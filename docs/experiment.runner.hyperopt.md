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
_summary_ The HyperOptRunner Implementation.  



<a href="../klops/experiment/runner/hyperopt.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Any,
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    x_test: Union[ndarray, DataFrame, List[Dict]],
    y_test: Union[ndarray, DataFrame, List],
    search_spaces: Dict,
    experiment_name: str,
    max_evals: int = 20
) → None
```

_summary_ 



**Args:**
 
 - <b>`estimator`</b> (Any):  _description_ 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List]):  _description_ 
 - <b>`search_spaces`</b> (Dict):  _description_ 
 - <b>`experiment_name`</b> (str):  _description_ 
 - <b>`max_evals`</b> (int, optional):  _description_. Defaults to 20. 




---

<a href="../klops/experiment/runner/hyperopt.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `objective`

```python
objective(hyper_parameters: Dict) → Dict
```

_summary_ 



**Returns:**
 
 - <b>`Dict`</b>:  _description_ 

---

<a href="../klops/experiment/runner/hyperopt.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
