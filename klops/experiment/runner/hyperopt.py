"""_summary_
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
    """_summary_

    Args:
        BaseRunner (_type_): _description_
    """

    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 x_test: Union[np.ndarray, pd.DataFrame, List[Dict]],
                 y_test: Union[np.ndarray, pd.DataFrame, List],
                 search_spaces: Dict,
                 experiment_name: str,
                 max_evals: int = 20) -> None:
        self.estimator = estimator
        self.search_spaces = search_spaces
        self.max_evals = max_evals
        self.experiment_name = experiment_name

        super(HyperOptRunner, self).__init__(
            estimator=estimator, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)

    def objective(self, hyper_parameters: Dict) -> Dict:
        """_summary_

        Returns:
            Dict: _description_
        """
        run_name = self.experiment_name + "_" + datetime.now().strftime("%Y%m%d:%H%M%S")
        with mlflow.start_run(run_name=run_name):

            mlflow.set_tags({
                "estimator_name": self.estimator.__class__.__name__,
                "opt": "hyperopt"
            })
            mlflow.log_params(hyper_parameters)
            model = self.estimator
            model.fit(self.x_train, self.y_train)
            preds = model.predict(self.x_test)
            rmse = metrics.mean_squared_error(
                self.y_test, preds, squared=False)
            for metric, arguments in self.metrices.items():
                self.call_metrices(metric, self.y_test, preds, **arguments)
            return {"loss": rmse, "status": STATUS_OK}

    def run(self,
            metrices: Dict = {"mean_squared_error": {},
                              "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """_summary_
        Run the experiment using hyperopt.fmin function.
        Args:
            metrices (_type_, optional): _description_.
                Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.
                The sklearn metrices. All metrices method name could be seen here:
                https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
        """
        try:

            self.metrices = metrices
            fmin(
                fn=self.objective,
                space=self.search_spaces,
                max_evals=self.max_evals,
                **kwargs
            )
        except Exception as exception:
            raise ExperimentFailedException(
                message=str(exception)) from exception
