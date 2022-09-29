"""
Main module for versioning Control.
"""
import csv
import json

from os.path import splitext
import pickle
from typing import Any, List

import yaml


import dvc

from klops.config import LOGGER
from klops.versioning.helper import shell_executor


class Versioning:
    """
    Versioning control for klops. Based on DVC.
    """

    def init(self) -> None:
        """Initiate DVC

        Initiate the DVC when it's not found.
        """
        shell_executor("dvc init")

    def add_remote(self, name: str, remote_url: str) -> None:
        """
        Add remote repository. Could be local, or remote storage such as GCP bucket or AWS s3.
        Args:
            remote_url (str): The remove URL for the DVC remote repository.
        """
        shell_executor(f"dvc remote add -d {name} {remote_url}")

    def add(self, file_or_path: str) -> None:
        """
        Track the file / path into DVC.
        Args:
            file_or_path (str):  File or path tobe added.
        """
        shell_executor(f"dvc add {file_or_path}")

    def push(self) -> None:
        """
        Push every tracked changes into dvc.
        """
        shell_executor("dvc push")

    def pull(self) -> None:
        """
        Pull the commited data.
        """
        shell_executor("dvc pull")

    def repro(self) -> None:
        """
        Reproduce the DVC pipeline.
        """
        shell_executor("dvc repro")

    def run(self,
            entry_point: str,
            name: str = None,
            dependencies: List = [],
            outputs: List = []) -> None:
        """
        Run the defined DVC pipeline.
        Args:
            entry_point (str):  The main program to be executed.
            name (str, optional): Defaults to None. The Pipeline name.
            dependencies (List, optional): Defaults to []. List of dependencies. \
                The same as `-d` options in dvc command.
            outputs (List, optional): Defaults to []. List of the outputs, The same as `-o` \
                options in dvc command.
        """
        deps = ""
        outs = ""
        name = "" if name is None else f" -n {name}"
        for dep in dependencies:
            deps = deps + "-d " + dep

        for out in outputs:
            outs = outs + "-o " + out

        shell_executor(f"dvc run{name} {deps} {outs} {entry_point}")

    def read_binary(self, file_name: str) -> Any:
        """
        Read the binary file such as .pkl, .joblib, etc. stored in the DVC storage / repository.
        Args:
            file_name (str):  The file name. Including its path.

        Returns:
            Any:  Object pointer instances.
        """
        try:
            model = pickle.loads(dvc.api.read(file_name, mode='rb'))
            return model
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))

    def read_dataset(self,
                     file_name: str,
                     rev: str = None,
                     remote: str = None) -> Any:
        """
        Read dataset from DVC artifact storage.
        Args:
            file_name (str): The file name. Including it's path.
            rev (str, optional): Revision or tags that already defined in git. Defaults to None.
            remote (str, optional): Remote repository URL. Defaults to None.
        Returns:
            Any:  The dataset file buffer. Need to parse.
        """
        try:
            with dvc.api.open(file_name, rev=rev, remote=remote) as file_buffer:
                name, extension = splitext(file_name)
                LOGGER.info("Reading file %s with extension %s", name, extension)
                if extension in [".csv", ".json", ".yaml", ".yml"]:
                    if extension == ".csv":
                        return csv.reader(file_buffer)
                    elif extension == ".json":
                        return json.load(file_buffer)
                    elif extension in [".yml", ".yaml"]:
                        return yaml.safe_load(file_buffer)
                else:
                    LOGGER.warning("Unsupported file extension: %s, \
                                   this would be return as a buffer.", extension)
                    return file_buffer
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))

    def get_url(self,
                path: str,
                repo: str = None,
                rev: str = None,
                remote: str = None) -> Any:
        """Get the URL to the storage location of a data file or \
            directory tracked in a DVC project.

        Args:
            path (str): Path to the data file or directory.
            repo (str, optional): Repository URL. Defaults to None.
            rev (str, optional): Revision or tags that already defined in git. Defaults to None.
            remote (str, optional): Remote URL for the repository. Defaults to None.

        Returns:
            Any: Returns the URL string of the storage location (in a DVC remote) \
                where a target file or directory, specified by its path in a repo \
                    (DVC project), is stored.
        """
        return dvc.api.get_url(path, repo, rev, remote)
