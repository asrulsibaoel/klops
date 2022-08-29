"""
Main module for Klops MLflow Experiment.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union
import os
import warnings

import joblib
import pandas as pd
import mlflow
import numpy as np
from mlflow.tracking import MlflowClient

from klops.experiment.runner import BasicRunner, GridsearchRunner, HyperOptRunner


warnings.filterwarnings(action="ignore")

class Experiment:
    """_summary_
    Main class for MLflow Experiment
    """

    def __init__(self, name: str,
                 tracking_uri: str = os.getenv("MLFLOW_TRACKING_URI", None)) -> None:
        self.name = name
        self.tracking_uri = tracking_uri
        os.environ["MLFLOW_TRACKING_URI"] = tracking_uri
        self.mlflow_client = MlflowClient()

        mlflow.set_experiment(name)

    def start(self,
              classifier: Any,
              x_train_data: Union[np.ndarray, pd.DataFrame, List[Dict]],
              y_train_data: Union[np.ndarray, pd.DataFrame, List],
              tuner: str = None,
              tuner_args: Dict = {},
              metrices: Dict = {
                  "mean_squared_error": {},
                  "root_mean_squared_error": {"squared": True}},
              **kwargs: Any) -> Experiment:
        """_summary_

        Args:
            classifier (Any): _description_
            x_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]): _description_
            y_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]): _description_
            tuner (None): _description_
            tuner_args (Dict, optional): _description_. Defaults to {}.
            metrices (_type_, optional): _description_. Defaults to
                { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.

        Raises:
            ValueError: _description_

        Returns:
            Experiment: _description_
        """

        if "tags" in kwargs:
            if isinstance(kwargs["tags"], Dict):
                mlflow.set_tags(kwargs["tags"])
                del kwargs["tags"]
            else:
                raise ValueError(
                    "Tags should be a dictionary with key-value pair.")

        if tuner in ["basic", None, "default"]:
            runner = BasicRunner(estimator=classifier,
                                 x_train=x_train_data,
                                 y_train=y_train_data,
                                 hyparams=tuner_args)
        elif tuner == "hyperopt":
            runner = HyperOptRunner(estimator=classifier,
                                    x_train=x_train_data,
                                    y_train=y_train_data,
                                    search_spaces=tuner_args)
        elif tuner == "gridsearch":
            runner = GridsearchRunner(estimator=classifier,
                                      x_train=x_train_data,
                                      y_train=y_train_data,
                                      grid_params=tuner_args)

        runner.run(metrices, **kwargs)

        return self

    def store_artifact(self, model: Any, local_path: str, artifact_path: str) -> None:
        """_summary_

        Args:
            model (Any): _description_
            local_path (str): _description_
            artifact_path (str): _description_
        """

        joblib.dump(model, local_path)

        mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)

    def log_param(self, key: str, value: str) -> None:
        """_summary_
        Log the parameters into the MLflow registry logs.
        Args:
            key (str): _description_
            value (str): _description_
        """
        mlflow.log_param(key=key, value=value)

    def log_metric(self, key: str, value: float) -> None:
        """_summary_

        Args:
            key (str): _description_
            value (Any): _description_
        """
        mlflow.log_metric(key=key, value=value)


def start_experiment(
        name: str,
        tracking_uri: str,
        classifier: Any,
        x_train_data: Union[np.ndarray, pd.DataFrame, List[Dict]],
        y_train_data: Union[np.ndarray, pd.DataFrame, List[Dict]],
        tuner: str = None,
        tuner_args: Dict = {},
        metrices: Dict = {
            "mean_squared_error": {},
            "root_mean_squared_error": {"squared": True}}
) -> Experiment:
    """_summary_

    Args:
        name (str): _description_
        tracking_uri (str): _description_
        classifier (Any): _description_
        x_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]): _description_
        y_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]): _description_
        tuner (None): _description_
        tuner_args (Dict, optional): _description_. Defaults to {}.
        metrices (_type_, optional): _description_.
            Defaults to { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.

    Returns:
        Experiment: _description_
    """
    experiment = Experiment(name=name, tracking_uri=tracking_uri)
    experiment.start(classifier=classifier, x_train_data=x_train_data,
                     y_train_data=y_train_data, tuner=tuner,
                     tuner_args=tuner_args, metrices=metrices)

    return experiment