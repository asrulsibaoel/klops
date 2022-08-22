<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/gridsearch_runner.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.gridsearch_runner`
_summary_ 



---

<a href="../klops/experiment/runner/gridsearch_runner.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GridsearchRunner`
_summary_ 



**Args:**
 
 - <b>`BaseRunner`</b> (_type_):  _description_ 

<a href="../klops/experiment/runner/gridsearch_runner.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Any,
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    grid_params: Dict = {},
    autolog_max_tunning_runs: int = None
) → None
```








---

<a href="../klops/experiment/runner/gridsearch_runner.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    metrices: Dict = {'mean_squared_error': {}, 'root_mean_squared_error': {}},
    **kwargs: Any
) → Any
```

_summary_ 



**Args:**
 
 - <b>`metrices`</b> (_type_, optional):  _description_. Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}. 



**Returns:**
 
 - <b>`Any`</b>:  _description_ 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
