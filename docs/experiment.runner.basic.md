<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/basic.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.basic`
_summary_ Experiment Runner Module without tuner. 



---

<a href="../klops/experiment/runner/basic.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BasicRunner`
_summary_ Experiment Runner Implementation Class without tuner. 

<a href="../klops/experiment/runner/basic.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Any,
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    x_test: Union[ndarray, DataFrame, List[Dict]],
    y_test: Union[ndarray, DataFrame, List],
    hyparams: Dict = {},
    autolog_max_tunning_runs: int = None
) → None
```

_summary_ 



**Args:**
 
 - <b>`estimator`</b> (Any):  _description_ 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List]):  _description_ 
 - <b>`hyparams`</b> (Dict, optional):  _description_. Defaults to {}. 
 - <b>`autolog_max_tunning_runs`</b> (int, optional):  _description_. Defaults to None. 




---

<a href="../klops/experiment/runner/basic.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    metrices: Dict = {'mean_squared_error': {}, 'root_mean_squared_error': {}},
    **kwargs: Any
) → Any
```

_summary_ Run the experiment without any tuner. 

**Args:**
 
 - <b>`metrices`</b> (_type_, optional):  _description_. 
 - <b>`Defaults to {"mean_squared_error"`</b>:  {}, "root_mean_squared_error": {}}. The sklearn metrices. All metrices method name could be seen here: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
