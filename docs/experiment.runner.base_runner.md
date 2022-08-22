<!-- markdownlint-disable -->

<a href="../klops/experiment/runner/base_runner.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.runner.base_runner`
_summary_ Base runner module 



---

<a href="../klops/experiment/runner/base_runner.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseRunner`
_summary_ 



**Args:**
 
 - <b>`ABC`</b> (_type_):  _description_ 

<a href="../klops/experiment/runner/base_runner.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict]
) → None
```








---

<a href="../klops/experiment/runner/base_runner.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `call_metrices`

```python
call_metrices(metric_name: str, *args, **kwargs: Any) → None
```

_summary_ Call the measurement metrices (inherited from sklearn metrices), log as mlflow metric. 

**Args:**
 
 - <b>`metric_name`</b> (str):  _description_ 

---

<a href="../klops/experiment/runner/base_runner.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(metrices: Dict, **kwargs: Any) → Any
```

_summary_ 



**Args:**
 
 - <b>`metrices`</b> (Dict):  _description_ 



**Returns:**
 
 - <b>`Any`</b>:  _description_ 

---

<a href="../klops/experiment/runner/base_runner.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split_train_test`

```python
split_train_test(
    x_train: Union[DataFrame, ndarray, List, Dict],
    y_train: Union[DataFrame, ndarray, List, Dict],
    test_size: float = 0.2,
    random_state: int = 11
) → None
```

_summary_ 



**Args:**
 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  _description_ 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
