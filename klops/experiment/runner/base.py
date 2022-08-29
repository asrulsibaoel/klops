"""_summary_
Base runner module
"""


from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

import mlflow
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split

from klops.experiment.exception import InvalidArgumentsException, LogMetricException


class BaseRunner(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    metrices: Dict = {"mean_squared_error": {}, "root_mean_squared_error": {}}

    def __init__(self, x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         y_train: Union[pd.DataFrame, np.ndarray, List, Dict]) -> None:
        self.split_train_test(x_train=x_train, y_train=y_train)

    @abstractmethod
    def run(self, metrices: Dict, **kwargs: Any) -> Any:
        """_summary_

        Args:
            metrices (Dict): _description_

        Returns:
            Any: _description_
        """

    def split_train_test(self,
                         x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         test_size: float = .2, random_state: int = 11) -> None:
        """_summary_

        Args:
            x_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
            y_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x_train, y_train, test_size=test_size, random_state=random_state)

    def call_metrices(self, metric_name: str, *args: Any, **kwargs: Any) -> None:
        """_summary_
        Call the measurement metrices (inherited from sklearn metrices), log as mlflow metric.
        Args:
            metric_name (str): _description_
        """
        try:
            if metric_name != "root_mean_squared_error":

                metric_function = getattr(metrics, metric_name)
                score = metric_function(*args, **kwargs)
            else:
                score = metrics.mean_squared_error(*args, **kwargs)
            mlflow.log_metric(metric_name, score)
        except ValueError as value_error:
            raise InvalidArgumentsException(message=str(value_error)) from value_error
        except Exception as exception:
            raise LogMetricException(message=str(exception)) from exception
