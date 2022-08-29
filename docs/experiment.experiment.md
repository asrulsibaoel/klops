<!-- markdownlint-disable -->

<a href="../klops/experiment/experiment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.experiment`
Main module for Klops MLflow Experiment. 

**Global Variables**
---------------
- **klops_path**

---

<a href="../klops/experiment/experiment.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

_summary_ The function that wrap all the basic Experiment class do. This make the process more easier. 



**Args:**
 
 - <b>`name`</b> (str):  _description_ The experiment name. Example: "my-classification-experiment" 
 - <b>`tracking_uri`</b> (str):  _description_ The MLflow experiment tracking uri.             Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>" 
 - <b>`classifier`</b> (Any):  _description_ The classifier pointer class.             Example: sklearn.naive_bayes.GaussianNB 
 - <b>`x_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              _description_ The input features with 2 Dimensional Array like. 
 - <b>`y_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              _description_ The output mapping. 
 - <b>`tuner`</b> (str):  _description_ The tuner could be one of (default | hyperopt | gridsearch).             Defaults to None. 
 - <b>`tuner_args`</b> (Dict, optional):  _description_. Defaults to {}. Tunner keyworded arguments.             A Dictionary contains key-value pairs set of hyper parameters. 
 - <b>`metrices`</b> (_type_, optional):  _description_. Defaults to             { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.             The sklearn metrices. All metrices method name could be seen here:             https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 



**Raises:**
 
 - <b>`ValueError`</b>:  _description_ Raised when the `tags` arguments has invalid value. 



**Returns:**
 
 - <b>`Experiment`</b>:  _description_ The itself class. 


---

<a href="../klops/experiment/experiment.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Experiment`
_summary_ Main class for MLflow Experiment. This class would wrap the MLFlow client and     it's experiments features. 

<a href="../klops/experiment/experiment.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: 'str', tracking_uri: 'str' = None) → None
```

_summary_ The Experiment class constructor. Every arguments sets here,         would be implemented to all experiments with the same name. 

**Args:**
 
 - <b>`name`</b> (str):  _description_ The experiment name. Example: "my-classification-experiment" 
 - <b>`tracking_uri`</b> (str):  _description_ The MLflow experiment tracking uri.                 Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>" 




---

<a href="../klops/experiment/experiment.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deploy`

```python
deploy(
    artifact_uri: 'str',
    deployment_name: 'str',
    model_name: 'str',
    authentication: 'AbstractKubernetesAuth',
    namespace: 'str' = 'default',
    deployment_template: 'str' = None
) → Dict
```

_summary_ Deploy experiment to Seldon Environment. 

This method would invoke the Deployment class and its dependencies to deploy the experiment using default / user defined template. 



**Args:**
 
 - <b>`artifact_uri`</b> (str):  _description_ The artifact URI.                 We could see it in the MLflow Tracking Server UI. 


 - <b>`deployment_name`</b> (str):  _description_ The Kubernetes deployment name. 
 - <b>`model_name`</b> (str):  _description_ The model name. 
 - <b>`authentication`</b> (AbstractKubernetesAuth):  _description_ The authentication object.                 Currently supports for GCP and default / minikube Auth. 
 - <b>`namespace`</b> (str, optional):  _description_. Defaults to 'default'.                 The Kubernetes target namespace. 
 - <b>`deployment_template`</b> (str, optional):  _description_. Defaults to None.                 Kubernetes JSON template file path. Recommended using default template. 

---

<a href="../klops/experiment/experiment.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_metric`

```python
log_metric(key: 'str', value: 'float') → None
```

_summary_ Log the metric into the MLflow Experiment logs. 

**Args:**
 
 - <b>`key`</b> (str):  _description_ The metric key. 
 - <b>`value`</b> (Any):  _description_ The metric value. 

---

<a href="../klops/experiment/experiment.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_param`

```python
log_param(key: 'str', value: 'str') → None
```

_summary_ Log the parameters into the MLflow Experiment logs. 

**Args:**
 
 - <b>`key`</b> (str):  _description_ The param key. 
 - <b>`value`</b> (str):  _description_ The param value. 

---

<a href="../klops/experiment/experiment.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start`

```python
start(
    classifier: 'Any',
    x_train_data: 'Union[ndarray, DataFrame, List[Dict]]',
    y_train_data: 'Union[ndarray, DataFrame, List]',
    tuner: 'str' = None,
    tuner_args: 'Dict' = {},
    metrices: 'Dict' = {'mean_squared_error': {}, 'root_mean_squared_error': {'squared': False}},
    **kwargs: 'Any'
) → Experiment
```

_summary_ Start the experiment given the arguments. 

**Args:**
 
 - <b>`classifier`</b> (Any):  _description_ The classifier pointer class.                 Example: sklearn.naive_bayes.GaussianNB 
 - <b>`x_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  _description_ The input features with 2 Dimensional Array like. 
 - <b>`y_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  _description_ The output mapping. 
 - <b>`tuner`</b> (str):  _description_ The tuner could be one of (default | hyperopt | gridsearch).                 Defaults to None. 
 - <b>`tuner_args`</b> (Dict, optional):  _description_. Defaults to {}. Tunner keyworded arguments.                 A Dictionary contains key-value pairs set of hyper parameters. 
 - <b>`metrices`</b> (_type_, optional):  _description_. Defaults to                 { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.                 The sklearn metrices. All metrices method name could be seen here:                 https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 



**Raises:**
 
 - <b>`ValueError`</b>:  _description_ Raised when the `tags` arguments has invalid value. 



**Returns:**
 
 - <b>`Experiment`</b>:  _description_ The itself class. 

---

<a href="../klops/experiment/experiment.py#L115"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `store_artifact`

```python
store_artifact(model: 'Any', local_path: 'str', artifact_path: 'str') → None
```

_summary_ Store the artifact into a joblib file. Then upload to the artifact registry. 

**Args:**
 
 - <b>`model`</b> (Any):  _description_ The model instance. 
 - <b>`local_path`</b> (str):  _description_ The local_path to be dump. 
 - <b>`artifact_path`</b> (str):  _description_ The artifact path in cloud storage. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
