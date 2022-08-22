"""_summary_
"""
from typing import Any, Union, List, Dict
import mlflow
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV

from klops.experiment.runner import BaseRunner


class GridsearchRunner(BaseRunner):
    """_summary_

    Args:
        BaseRunner (_type_): _description_
    """

    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 grid_params: Dict = {},
                 autolog_max_tunning_runs: int = None) -> None:
        self.grid_params = grid_params
        self.estimator = estimator
        mlflow.sklearn.autolog(max_tuning_runs=autolog_max_tunning_runs)
        mlflow.set_tags({
            "opt": "grid-search",
            "model": self.estimator.__class__.__name__
        })
        super(GridsearchRunner, self).__init__(
            x_train=x_train, y_train=y_train)

    def run(self,
            metrices: Dict = {"mean_squared_error": {}, "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """_summary_

        Args:
            metrices (_type_, optional): _description_. Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.

        Returns:
            Any: _description_
        """

        model = self.estimator()
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=self.grid_params,
            **kwargs
        )
        best_fit = grid_search.fit(self.x_train, self.y_train)
        preds = best_fit.predict(self.x_test)
        for metric, arguments in metrices.items():
            self.call_metrices(metric, self.y_test, preds, **arguments)
