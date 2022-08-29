"""_summary_
Main module for versioning Control.
"""

import pickle
from typing import Any, Dict, List, Union

import dvc
import numpy as np
import pandas as pd

from klops.config import LOGGER
from klops.versioning.helper import shell_executor


class Versioning:
    """_summary_
    Versioning control for klops. Based on DVC.
    """

    def init(self) -> None:
        """_summary_ Initiate DVC

        Initiate the DVC when it's not found.
        """
        shell_executor("dvc init")

    def add_remote(self, name: str, remote_url: str) -> None:
        """_summary_
        Add remote repository.
        Args:
            remote_url (str): _description_
        """
        shell_executor(f"dvc remote add -d {name} {remote_url}")

    def add(self, file_or_path: str) -> None:
        """_summary_
        Track the file / path into DVC.
        Args:
            file_or_path (str): _description_ File or path tobe added.
        """
        shell_executor(f"dvc add {file_or_path}")

    def push(self) -> None:
        """_summary_
        Push changes into dvc
        """
        shell_executor("dvc push")

    def run(self,
            entry_point: str,
            name: str = None,
            dependencies: List = [],
            outputs: List = []) -> None:
        """_summary_

        Args:
            entry_point (str): _description_
            name (str, optional): _description_. Defaults to None.
            dependencies (List, optional): _description_. Defaults to [].
            outputs (List, optional): _description_. Defaults to [].
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
        """_summary_

        Args:
            file_name (str): _description_

        Returns:
            Any: _description_
        """
        try:
            model = pickle.loads(dvc.api.read(file_name, mode='rb'))
            return model
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))

    def read_dataset(self, file_name: str) -> Union[List, Dict, pd.DataFrame, np.ndarray]:
        """_summary_

        Args:
            file_name (str): _description_

        Returns:
            Union[List, Dict, pd.DataFrame, np.ndarray]: _description_
        """
        try:
            with dvc.api.open(file_name) as file_buffer:
                return file_buffer
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))
