"""
"""
from typing import Any, Dict, List, Union
from datetime import datetime

from hyperopt import STATUS_OK, fmin
import mlflow
import numpy as np
import pandas as pd
from sklearn import metrics

from klops.experiment.runner import BaseRunner
from klops.experiment.exception import ExperimentFailedException


class HyperOptRunner(BaseRunner):
    """The HyperOptRunner Implementation.
    """

    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 x_test: Union[np.ndarray, pd.DataFrame, List[Dict]],
                 y_test: Union[np.ndarray, pd.DataFrame, List],
                 search_spaces: Dict,
                 experiment_name: str,
                 tags: Dict = {},
                 max_evals: int = 20) -> None:
        """

        Args:
            estimator (Any): The model class instance. Can be sklearn model or any of supported \
                models by mlflow.
            x_train (Union[pd.DataFrame, np.ndarray, List, Dict]): The features set for training.
            y_train (Union[pd.DataFrame, np.ndarray, List, Dict]): The target set for training.
            x_test (Union[np.ndarray, pd.DataFrame, List[Dict]]): The test features.
            y_test (Union[np.ndarray, pd.DataFrame, List]): The test expected target.
            search_spaces (Dict): Hyperparameter search space for training.
            experiment_name (str): The experiment name. Example: "my-experiment-name".
            max_evals (int, optional):  Defaults to 20. Maximum number of training trials.
        """
        self.search_spaces = search_spaces
        self.max_evals = max_evals
        self.experiment_name = experiment_name

        super(HyperOptRunner, self).__init__(
            estimator=estimator, x_train=x_train, y_train=y_train,
            x_test=x_test, y_test=y_test, tags=tags)

    def objective(self, hyper_parameters: Dict) -> Dict:
        """
        Run the experiment using hyperopt. Each experiment would generate exactly one \
            artifact regitry in repository.

        Args:
            hyper_parameters (Dict): The hyper parameters for each experiment.

        Returns:
            Dict: Dictionary contains error function result.
        """
        run_name = self.experiment_name + "_" + datetime.now().strftime("%Y%m%d:%H%M%S")
        with mlflow.start_run(run_name=run_name):
            result = {"status": STATUS_OK}

            mlflow.set_tags({**self.tags, "opt":"hyperopt"})
            mlflow.log_params({
                **hyper_parameters,
                "estimator": self.estimator.__class__.__name__})

            model = self.estimator
            model.fit(self.x_train, self.y_train)
            preds = model.predict(self.x_test)
            rmse = self.call_metrices("rmse", self.y_test, preds)
            for metric, arguments in self.metrices.items():
                metric_name, score = self.call_metrices(metric, self.y_test, preds, **arguments)
                result[metric_name] = score
            return {**result, "loss": rmse}

    def run(self,
            metrices: Dict = {"mean_squared_error": {},
                              "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """
        Run the experiment using hyperopt.fmin function.

        Args:
            metrices (_type_, optional):
                Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.
                The sklearn metrices. All metrices method name could be seen here:
                https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
        """
        try:

            self.metrices = metrices
            best_fit = fmin(
                fn=self.objective,
                space=self.search_spaces,
                max_evals=self.max_evals,
                **kwargs
            )

            return best_fit
        except Exception as exception:
            raise ExperimentFailedException(
                message=str(exception)) from exception


__all__ = ["HyperOptRunner"]
