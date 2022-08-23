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

from klops.config import LOGGER


class BaseRunner(ABC):
    """_summary_
    Abstract class as Base runner implementation.
    """
    def __init__(self, x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         y_train: Union[pd.DataFrame, np.ndarray, List, Dict]) -> None:
        self.split_train_test(x_train=x_train, y_train=y_train)

    @abstractmethod
    def run(self, metrices: Dict, **kwargs: Any) -> Any:
        """_summary_
        The abstract method for base implementation to execute the experiment.
        Args:
            metrices (Dict): _description_ The metrices that would be invoked as measurements.
            **kwargs (Any): _description_ The key-word arguments hyper-parameters for the given class Model.
        Returns:
            Any: _description_
        """

    def split_train_test(self,
                         x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                         test_size: float = .2, random_state: int = 11) -> None:
        """_summary_
        Splits the given datasets of features and its class into train-test group pair.
        Args:
            x_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
                The features data.
            y_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
                The class data.
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x_train, y_train, test_size=test_size, random_state=random_state)

    def call_metrices(self, metric_name: str, *args, **kwargs: Any) -> None:
        """_summary_
        Call the measurement metrices (inherited from sklearn metrices), log as mlflow metric.
        Args:
            metric_name (str): _description_ The sklearn metrices.
            All metrices method name could be seen here:
            https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
        """
        try:
            if metric_name != "root_mean_squared_error":

                metric_function = getattr(metrics, metric_name)
                score = metric_function(*args, **kwargs)
            else:
                score = metrics.mean_squared_error(*args, **kwargs)
            mlflow.log_metric(metric_name, score)
        except ValueError as value_error:
            LOGGER.error(str(value_error))
        except Exception as exception:
            LOGGER.error(str(exception))
