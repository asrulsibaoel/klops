"""_summary_
"""
from typing import Any, Dict, List, Union

from hyperopt import STATUS_OK, fmin
import mlflow
import numpy as np
import pandas as pd
from sklearn import metrics

from klops.experiment.runner import BaseRunner


class HyperOptRunner(BaseRunner):
    """_summary_

    Args:
        BaseRunner (_type_): _description_
    """

    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 search_spaces: Dict,
                 max_evals: int = 20) -> None:
        self.estimator = estimator
        self.search_spaces = search_spaces
        self.max_evals = max_evals
        mlflow.set_tags({
                "model": self.estimator.__name__,
                "opt": "hyperopt"
            })
        super(HyperOptRunner, self).__init__(x_train=x_train, y_train=y_train)

    def objective(self, **kwargs: Any) -> Dict:
        """_summary_

        Returns:
            Dict: _description_
        """
        metrices = {"mean_squared_error": {}, "root_mean_squared_error": {"squared": False}}
        if "metrices" in kwargs:
            metrices = kwargs["metrices"]
            del kwargs["metrices"]
        hyper_parameters = kwargs
        with mlflow.start_run():
            mlflow.log_params(hyper_parameters)
            model = self.estimator(
                **hyper_parameters
            )
            model.fit(self.x_train, self.y_train)
            preds = model.predict(self.x_test)
            rmse = metrics.mean_squared_error(self.y_test, preds, squared=False)
            for metric in metrices:
                self.call_metrices(metric, self.y_test, preds, **metric)
        return {"loss": rmse, "status": STATUS_OK}

    def run(self,
            metrices: Dict = {"mean_squared_error": {}, "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """_summary_
        Run the experiment using hyperopt.fmin function.
        Args:
            metrices (_type_, optional): _description_.
                Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.
                The sklearn metrices. All metrices method name could be seen here:
                https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
        """
        fmin(
            fn=self.objective,
            space={**self.search_spaces, "metrices": metrices},
            max_evals=self.max_evals,
            **kwargs
        )
