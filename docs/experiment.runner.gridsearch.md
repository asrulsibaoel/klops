<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/gridsearch.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.gridsearch`
_summary_ 



---

<a href="../klops/experiment/runner/gridsearch.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GridsearchRunner`
_summary_ GridSearchCV Runner Implementation.  



<a href="../klops/experiment/runner/gridsearch.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Type[Any],
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    x_test: Union[ndarray, DataFrame, List[Dict]],
    y_test: Union[ndarray, DataFrame, List],
    grid_params: Dict = {},
    autolog_max_tunning_runs: int = None
) → None
```

_summary_ 



**Args:**
 
 - <b>`estimator`</b> (Type[Any]):  _description_ 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List]):  _description_ 
 - <b>`grid_params`</b> (Dict, optional):  _description_. Defaults to {}. 
 - <b>`autolog_max_tunning_runs`</b> (int, optional):  _description_. Defaults to None. 




---

<a href="../klops/experiment/runner/gridsearch.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    metrices: Dict = {'mean_squared_error': {}, 'root_mean_squared_error': {}},
    **kwargs: Any
) → Any
```

_summary_ Run the experiment using sklearn.model_selection.GridsearchCV tuner. 

**Args:**
 
 - <b>`metrices`</b> (_type_, optional):  _description_. 
 - <b>`Defaults to {"mean_squared_error"`</b>:  {}, "root_mean_squared_error": {}}. The sklearn metrices. All metrices method name could be seen here: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
