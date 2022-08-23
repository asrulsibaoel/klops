"""_summary_
Experiment Runner Module without tuner.
"""

from typing import Any, Union, List, Dict
import mlflow
import numpy as np
import pandas as pd

from klops.experiment.runner.base import BaseRunner


class BasicRunner(BaseRunner):
    """_summary_
    Experiment Runner Implementation Class without tuner.
    Inherited:
        BaseRunner (_type_): _description_
    """
    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 hyparams: Dict = {},
                 autolog_max_tunning_runs: int = None) -> None:
        self.hyparams = hyparams
        self.estimator = estimator
        mlflow.sklearn.autolog(max_tuning_runs=autolog_max_tunning_runs)
        mlflow.set_tags({
            "opt": "basic",
            "model": self.estimator.__class__.__name__
        })
        super(BasicRunner, self).__init__(x_train=x_train, y_train=y_train)

    def run(self,
            metrices: Dict = {"mean_squared_error": {}, "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """_summary_

        Args:
            metrices (_type_, optional): _description_.
                Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.

        Returns:
            Any: _description_
        """
        with mlflow.start_run(run_name="test run"):
            mlflow.log_params(kwargs)
            model = self.estimator(
                **kwargs
            )

            model.fit(self.x_train, self.y_train)
            preds = model.predict(self.x_test)
            for metric, arguments in metrices.items():
                self.call_metrices(metric, self.y_test, preds, **arguments)
