<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/hyperopt.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.hyperopt`
_summary_ 

**Global Variables**
---------------
- **STATUS_OK**


---

<a href="../klops/experiment/runner/hyperopt.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `HyperOptRunner`
_summary_ 



**Args:**
 
 - <b>`BaseRunner`</b> (_type_):  _description_ 

<a href="../klops/experiment/runner/hyperopt.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Any,
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    search_spaces: Dict,
    experiment_name: str,
    max_evals: int = 20
) → None
```








---

<a href="../klops/experiment/runner/hyperopt.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `objective`

```python
objective(hyper_parameters: Dict) → Dict
```

_summary_ 



**Returns:**
 
 - <b>`Dict`</b>:  _description_ 

---

<a href="../klops/experiment/runner/hyperopt.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    metrices: Dict = {'mean_squared_error': {}, 'root_mean_squared_error': {}},
    **kwargs: Any
) → Any
```

_summary_ Run the experiment using hyperopt.fmin function. 

**Args:**
 
 - <b>`metrices`</b> (_type_, optional):  _description_. 
 - <b>`Defaults to {"mean_squared_error"`</b>:  {}, "root_mean_squared_error": {}}. The sklearn metrices. All metrices method name could be seen here: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
