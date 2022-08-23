<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/base.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.base`
_summary_ Base runner module 



---

<a href="../klops/experiment/runner/base.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseRunner`
_summary_ Abstract class as Base runner implementation. 

<a href="../klops/experiment/runner/base.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict]
) → None
```








---

<a href="../klops/experiment/runner/base.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `call_metrices`

```python
call_metrices(metric_name: str, *args, **kwargs: Any) → None
```

_summary_ Call the measurement metrices (inherited from sklearn metrices), log as mlflow metric. 

**Args:**
 
 - <b>`metric_name`</b> (str):  _description_ The sklearn metrices. All metrices method name could be seen here: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 

---

<a href="../klops/experiment/runner/base.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(metrices: Dict, **kwargs: Any) → Any
```

_summary_ The abstract method for base implementation to execute the experiment. 

**Args:**
 
 - <b>`metrices`</b> (Dict):  _description_ The metrices that would be invoked as measurements. 
 - <b>`**kwargs (Any)`</b>:  _description_ The key-word arguments hyper-parameters for the given class Model. 

**Returns:**
 
 - <b>`Any`</b>:  _description_ 

---

<a href="../klops/experiment/runner/base.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split_train_test`

```python
split_train_test(
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    test_size: float = 0.2,
    random_state: int = 11
) → None
```

_summary_ Splits the given datasets of features and its class into train-test group pair. 

**Args:**
 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_  The features data. 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_  The class data. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
