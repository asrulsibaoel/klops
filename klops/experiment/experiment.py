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

import klops
from klops.config import LOGGER
from klops.seldon_core import SeldonDeployment
from klops.experiment.runner import BasicRunner, GridsearchRunner, HyperOptRunner
from klops.seldon_core.auth.schema import AbstractKubernetesAuth

klops_path = klops.__path__

warnings.filterwarnings(action="ignore")

class Experiment:
    """_summary_
    Main class for MLflow Experiment. This class would wrap the MLFlow client and
    it's experiments features.
    """

    def __init__(self, name: str,
                 tracking_uri: str = os.getenv("MLFLOW_TRACKING_URI", None)) -> None:
        """_summary_
        The Experiment class constructor. Every arguments sets here,
        would be implemented to all experiments with the same name.
        Args:
            name (str): _description_ The experiment name. Example: "my-classification-experiment"
            tracking_uri (str): _description_ The MLflow experiment tracking uri.
                Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>"
        """
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
                  "root_mean_squared_error": {"squared": False}},
              **kwargs: Any) -> Experiment:
        """_summary_
        Start the experiment given the arguments.
        Args:
            classifier (Any): _description_ The classifier pointer class.
                Example: sklearn.naive_bayes.GaussianNB
            x_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]):
                _description_ The input features with 2 Dimensional Array like.
            y_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]):
                _description_ The output mapping.
            tuner (str): _description_ The tuner could be one of (default | hyperopt | gridsearch).
                Defaults to None.
            tuner_args (Dict, optional): _description_. Defaults to {}. Tunner keyworded arguments.
                A Dictionary contains key-value pairs set of hyper parameters.
            metrices (_type_, optional): _description_. Defaults to
                { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.
                The sklearn metrices. All metrices method name could be seen here:
                https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics

        Raises:
            ValueError: _description_ Raised when the `tags` arguments has invalid value.

        Returns:
            Experiment: _description_ The itself class.
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
        Store the artifact into a joblib file. Then upload to the artifact registry.
        Args:
            model (Any): _description_ The model instance.
            local_path (str): _description_ The local_path to be dump.
            artifact_path (str): _description_ The artifact path in cloud storage.
        """

        joblib.dump(model, local_path)

        mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)

    def log_param(self, key: str, value: str) -> None:
        """_summary_
        Log the parameters into the MLflow Experiment logs.
        Args:
            key (str): _description_ The param key.
            value (str): _description_ The param value.
        """
        mlflow.log_param(key=key, value=value)

    def log_metric(self, key: str, value: float) -> None:
        """_summary_
        Log the metric into the MLflow Experiment logs.
        Args:
            key (str): _description_ The metric key.
            value (Any): _description_ The metric value.
        """
        mlflow.log_metric(key=key, value=value)

    def deploy(self,
               artifact_uri: str,
               deployment_name: str,
               model_name: str,
               authentication: AbstractKubernetesAuth,
               namespace: str = 'default',
               deployment_template: str = None) -> None:
        """_summary_
        Deploy experiment to Seldon Environment.
        Args:
            artifact_uri (str): _description_ The artifact URI.
                We could see it in the MLflow Tracking Server UI.
            deployment_name (str): _description_ The Kubernetes deployment name.
            model_name (str): _description_ The model name.
            authentication (AbstractKubernetesAuth): _description_ The authentication object.
                Currently supports for GCP and default / minikube Auth.
            namespace (str, optional): _description_. Defaults to 'default'.
                The Kubernetes target namespace.
            deployment_template (str, optional): _description_. Defaults to None.
                Kubernetes JSON template file path. Recommended using default template.
        """
        try:
            deployment = SeldonDeployment(
                authentication=authentication, namespace=namespace)
            if deployment_template is None:
                deployment_template = os.path.join(klops_path, 'templates/deployment_template.json')

            config = deployment.load_deployment_configuration(deployment_template)
            config["metadata"]["name"] = deployment_name
            config["spec"]["name"] = model_name
            config["spec"]["predictors"][0]["graph"]["modelUri"] = artifact_uri
            deployment.deploy(config)
        except Exception as exception:
            LOGGER.error("Deployment Failed. caused by: %s", str(exception))


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
    The function that wrap all the basic Experiment class do. This make the process more easier.

    Args:
        name (str): _description_ The experiment name. Example: "my-classification-experiment"
        tracking_uri (str): _description_ The MLflow experiment tracking uri.
            Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>"
        classifier (Any): _description_ The classifier pointer class.
            Example: sklearn.naive_bayes.GaussianNB
        x_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]):
            _description_ The input features with 2 Dimensional Array like.
        y_train_data (Union[np.ndarray, pd.DataFrame, List[Dict]]):
            _description_ The output mapping.
        tuner (str): _description_ The tuner could be one of (default | hyperopt | gridsearch).
            Defaults to None.
        tuner_args (Dict, optional): _description_. Defaults to {}. Tunner keyworded arguments.
            A Dictionary contains key-value pairs set of hyper parameters.
        metrices (_type_, optional): _description_. Defaults to
            { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.
            The sklearn metrices. All metrices method name could be seen here:
            https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
    Raises:
        ValueError: _description_ Raised when the `tags` arguments has invalid value.
    Returns:
        Experiment: _description_ The itself class.
    """
    experiment = Experiment(name=name, tracking_uri=tracking_uri)
    experiment = experiment.start(classifier=classifier, x_train_data=x_train_data,
                     y_train_data=y_train_data, tuner=tuner,
                     tuner_args=tuner_args, metrices=metrices)

    return experiment
