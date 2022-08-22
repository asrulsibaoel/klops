"""_summary_
"""
import subprocess

from klops.config import LOGGER


def shell_executor(command: str) -> subprocess.CompletedProcess:
    """_summary_
    Command line executor.
    Args:
        command (str): _description_ The command tobe executed.
    """
    try:
        return subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as called_error:
        LOGGER.error(str(called_error))
    except subprocess.SubprocessError as sub_error:
        LOGGER.error(str(sub_error))
    