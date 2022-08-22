<!-- markdownlint-disable -->

<a href="../klops/experiment/experiment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.experiment`
Main module for Klops MLflow Experiment. 


---

<a href="../klops/experiment/experiment.py#L153"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `start_experiment`

```python
start_experiment(
    name: 'str',
    tracking_uri: 'str',
    classifier: 'Any',
    x_train_data: 'Union[ndarray, DataFrame, List[Dict]]',
    y_train_data: 'Union[ndarray, DataFrame, List[Dict]]',
    tuner: 'str' = None,
    tuner_args: 'Dict' = {},
    metrices: 'Dict' = {'mean_squared_error': {}, 'root_mean_squared_error': {'squared': True}}
) → Experiment
```

_summary_ 



**Args:**
 
 - <b>`name`</b> (str):  _description_ 
 - <b>`tracking_uri`</b> (str):  _description_ 
 - <b>`classifier`</b> (Any):  _description_ 
 - <b>`x_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`tuner`</b> (None):  _description_ 
 - <b>`tuner_args`</b> (Dict, optional):  _description_. Defaults to {}. 
 - <b>`metrices`</b> (_type_, optional):  _description_. 
 - <b>`Defaults to { "mean_squared_error"`</b>:  {}, "root_mean_squared_error": {"squared": True}}. 



**Returns:**
 
 - <b>`Experiment`</b>:  _description_ 


---

<a href="../klops/experiment/experiment.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Experiment`
_summary_ Main class for MLflow Experiment 

<a href="../klops/experiment/experiment.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: 'str', tracking_uri: 'str') → None
```








---

<a href="../klops/experiment/experiment.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deploy`

```python
deploy(
    artifact_uri: 'str',
    deployment_name: 'str',
    model_name: 'str',
    authentication: 'AbstractKubernetesAuth',
    namespace: 'str' = 'default'
) → None
```

_summary_ 



**Args:**
 
 - <b>`artifact_uri`</b> (str):  _description_ 
 - <b>`deployment_name`</b> (str):  _description_ 
 - <b>`model_name`</b> (str):  _description_ 
 - <b>`authentication`</b> (AbstractKubernetesAuth):  _description_ 
 - <b>`namespace`</b> (str, optional):  _description_. Defaults to 'default'. 

---

<a href="../klops/experiment/experiment.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_metric`

```python
log_metric(key: 'str', value: 'float') → None
```

_summary_ 



**Args:**
 
 - <b>`key`</b> (str):  _description_ 
 - <b>`value`</b> (Any):  _description_ 

---

<a href="../klops/experiment/experiment.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_param`

```python
log_param(key: 'str', value: 'str') → None
```

_summary_ Log the parameters into the MLflow registry logs. 

**Args:**
 
 - <b>`key`</b> (str):  _description_ 
 - <b>`value`</b> (str):  _description_ 

---

<a href="../klops/experiment/experiment.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start`

```python
start(
    classifier: 'Any',
    x_train_data: 'Union[ndarray, DataFrame, List[Dict]]',
    y_train_data: 'Union[ndarray, DataFrame, List]',
    tuner: 'str' = None,
    tuner_args: 'Dict' = {},
    metrices: 'Dict' = {'mean_squared_error': {}, 'root_mean_squared_error': {'squared': True}},
    **kwargs: 'Any'
) → Experiment
```

_summary_ 



**Args:**
 
 - <b>`classifier`</b> (Any):  _description_ 
 - <b>`x_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`y_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):  _description_ 
 - <b>`tuner`</b> (None):  _description_ 
 - <b>`tuner_args`</b> (Dict, optional):  _description_. Defaults to {}. 
 - <b>`metrices`</b> (_type_, optional):  _description_. Defaults to  
 - <b>`{ "mean_squared_error"`</b>:  {}, "root_mean_squared_error": {"squared": True}}. 



**Raises:**
 
 - <b>`ValueError`</b>:  _description_ 



**Returns:**
 
 - <b>`Experiment`</b>:  _description_ 

---

<a href="../klops/experiment/experiment.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `store_artifact`

```python
store_artifact(model: 'Any', local_path: 'str', artifact_path: 'str') → None
```

_summary_ 



**Args:**
 
 - <b>`model`</b> (Any):  _description_ 
 - <b>`local_path`</b> (str):  _description_ 
 - <b>`artifact_path`</b> (str):  _description_ 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
