"""_summary_
"""
from typing import Any, Dict, List, Type, Union

from hyperopt import STATUS_OK, fmin
import mlflow
import numpy as np
import pandas as pd
from sklearn import metrics

from klops.experiment.runner import BaseRunner


class SpaceArguments:
    """_summary_ fmin spaces Arguments Defined object.
    The Defined Class to make sure the input arguments for objective is
    in the right pattern.
    """

    estimator: Type[Any] = None
    x_train: Union[pd.DataFrame, np.ndarray, List, Dict] = None
    y_train: Union[pd.DataFrame, pd.Series, np.ndarray, List, Dict] = None
    hyper_parameters: Dict = None
    metrices: Dict = {"mean_squared_error": {}, "root_mean_squared_error": {"squared": False}}


def objective(space_args: SpaceArguments) -> Dict:
    """_summary_ Hyperopt function runner.
    This is the main function to execute every experiment given the search spaces.

    Args:
        space_args (SpaceArguments): _description_ All the attributes must be provided.

    Returns:
        Dict: _description_ Metrics checking result.
    """
    with mlflow.start_run():
        mlflow.log_params(space_args.hyper_parameters)
        model = space_args.estimator(
            **space_args.hyper_parameters
        )
        model.fit(space_args.x_train, space_args.y_train)
        preds = model.predict(space_args.x_test)
        rmse = metrics.mean_squared_error(space_args.y_test, preds, squared=False)
        for metric in space_args.metrices:
            space_args.call_metrices(metric, space_args.y_test, preds, **metric)
    return {"loss": rmse, "status": STATUS_OK}


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

    # def objective(self, **hyper_parameters: Any) -> Dict:
    #     """_summary_

    #     Returns:
    #         Dict: _description_
    #     """
    #     with mlflow.start_run():
    #         mlflow.log_params(hyper_parameters)
    #         model = self.estimator(
    #             **hyper_parameters
    #         )
    #         model.fit(self.x_train, self.y_train)
    #         preds = model.predict(self.x_test)
    #         rmse = metrics.mean_squared_error(self.y_test, preds, squared=False)
    #         for metric in self.metrices:
    #             self.call_metrices(metric, self.y_test, preds, **metric)
    #     return {"loss": rmse, "status": STATUS_OK}

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
        spaces = SpaceArguments()
        spaces.x_train = self.x_train
        spaces.y_train = self.y_train
        spaces.estimator = self.estimator
        spaces.hyper_parameters = self.search_spaces
        fmin(
            fn=self.objective,
            space=self.search_spaces,
            max_evals=self.max_evals,
            **kwargs
        )
