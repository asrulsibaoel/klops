<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/base.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.base`
Base runner module. 



---

<a href="../klops/experiment/runner/base.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseRunner`
Abstract class as Base runner implementation. 

<a href="../klops/experiment/runner/base.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    estimator: Any,
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    x_test: Union[ndarray, DataFrame, List[Dict]],
    y_test: Union[ndarray, DataFrame, List],
    tags: Dict = {}
) → None
```



**Args:**
 
 - <b>`estimator`</b> (Any):  _description_ 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List]):  _description_ 
 - <b>`tags`</b> (Dict):  Defaults to {}. Additional tags for logging in Experiment. 




---

<a href="../klops/experiment/runner/base.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `call_metrices`

```python
call_metrices(metric_name: str, *args: Any, **kwargs: Any) → Tuple
```

Call the measurement metrices (inherited from sklearn metrices), log as mlflow metric. 

**Args:**
 
 - <b>`metric_name`</b> (str):  The sklearn metrices. All metrices method name could be seen here: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 

---

<a href="../klops/experiment/runner/base.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(metrices: Dict, **kwargs: Any) → Any
```

The abstract method for base implementation to execute the experiment. 

**Args:**
 
 - <b>`metrices`</b> (Dict):  The metrices that would be invoked as measurements. 
 - <b>`**kwargs (Any)`</b>:  The key-word arguments hyper-parameters for the given class Model. 

**Returns:**
 
 - <b>`Any`</b>:  _description_ 

---

<a href="../klops/experiment/runner/base.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split_train_test`

```python
split_train_test(
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    test_size: float = 0.2,
    random_state: int = 11
) → None
```

Splits the given datasets of features and its class into train-test group pair. 

**Args:**
 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  The features data. 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  The class data. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
