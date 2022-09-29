<!-- markdownlint-disable -->

<a href="../klops/experiment/experiment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.experiment`
Main module for Klops MLflow Experiment. 

**Global Variables**
---------------
- **KLOPS_PATH**

---

<a href="../klops/experiment/experiment.py#L269"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `start_experiment`

```python
start_experiment(
    name: 'str',
    tracking_uri: 'str',
    classifier: 'Any',
    x_train: 'Union[ndarray, DataFrame, List[Dict]]',
    y_train: 'Union[ndarray, DataFrame, List[Dict]]',
    dataset_auto_split: 'bool' = True,
    x_test: 'Union[ndarray, DataFrame, List[Dict]]' = [],
    y_test: 'Union[ndarray, DataFrame, List]' = [],
    test_size: 'float' = 0.2,
    random_state: 'int' = 11,
    tuner: 'str' = None,
    tuner_args: 'Dict' = {},
    metrices: 'Dict' = {'mean_squared_error': {}, 'root_mean_squared_error': {'squared': True}}
) → Experiment
```

The function that wrap all the basic Experiment class do. This make the process more easier. 



**Args:**
 
 - <b>`name`</b> (str):  The experiment name. Example: "my-classification-experiment" 
 - <b>`tracking_uri`</b> (str):  The MLflow experiment tracking uri.             Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>" 
 - <b>`classifier`</b> (Any):  The classifier pointer class.             Example: sklearn.naive_bayes.GaussianNB 
 - <b>`x_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              The input features with 2 Dimensional Array like. 
 - <b>`y_train_data`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              The output mapping. 
 - <b>`dataset_auto_split`</b> (bool):   Whether to automatically split the dataset into train-test pairs. 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              The input test value. Only usable when the dataset_auto_split flag is False. 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):              The output test value. Only usable when the dataset_auto_split flag is False. 
 - <b>`test_size`</b> (float):  The split size of the test data. 
 - <b>`random_state`</b> (int):  The number of random state. 
 - <b>`tuner`</b> (str):  The tuner could be one of (default | hyperopt | gridsearch).             Defaults to None. 
 - <b>`tuner_args`</b> (Dict, optional):   Defaults to {}. Tunner keyworded arguments.             A Dictionary contains key-value pairs set of hyper parameters. 
 - <b>`metrices`</b> (_type_, optional):   Defaults to             { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.             The sklearn metrices. All metrices method name could be seen here:             https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 



**Raises:**
 
 - <b>`ValueError`</b>:  Raised when the input arguments has invalid value. 



**Returns:**
 
 - <b>`Experiment`</b>:  The Experiment class instance. 


---

<a href="../klops/experiment/experiment.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Experiment`
Main class for MLflow Experiment. This class would wrap the MLFlow client and     it's experiments features. 

<a href="../klops/experiment/experiment.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: 'str', tracking_uri: 'str' = None) → None
```

The Experiment class constructor. Every arguments sets here,         would be implemented to all experiments with the same name. 

**Args:**
 
 - <b>`name`</b> (str):  The experiment name. Example: "my-classification-experiment" 
 - <b>`tracking_uri`</b> (str):  The MLflow experiment tracking uri.                 Its our MLflow Tracking server URI. Example: "http://<your-mlflow-host>:<port>" 




---

<a href="../klops/experiment/experiment.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

Deploy experiment to Seldon Environment. 

This method would invoke the Deployment class and its dependencies to deploy         the experiment using default / user defined template. 



**Args:**
 
 - <b>`artifact_uri`</b> (str):  The artifact URI.                 We could see it in the MLflow Tracking Server UI. 
 - <b>`deployment_name`</b> (str):  The Kubernetes deployment name. 
 - <b>`model_name`</b> (str):  The model name. 
 - <b>`authentication`</b> (AbstractKubernetesAuth):  The authentication object.                 Currently supports for GCP and default / minikube Auth. 
 - <b>`namespace`</b> (str, optional):   Defaults to 'default'.                 The Kubernetes target namespace. 
 - <b>`deployment_template`</b> (str, optional):   Defaults to None.                 Kubernetes JSON template file path. Recommended using default template. 

---

<a href="../klops/experiment/experiment.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_metric`

```python
log_metric(key: 'str', value: 'float') → None
```

Log the metric into the MLflow Experiment logs. 

**Args:**
 
 - <b>`key`</b> (str):  The metric key. 
 - <b>`value`</b> (Any):  The metric value. 

---

<a href="../klops/experiment/experiment.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log_param`

```python
log_param(key: 'str', value: 'str') → None
```

Log the parameters into the MLflow Experiment logs. 

**Args:**
 
 - <b>`key`</b> (str):  The param key. 
 - <b>`value`</b> (str):  The param value. 

---

<a href="../klops/experiment/experiment.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split_train_test`

```python
split_train_test(
    x_train: 'Union[DataFrame, ndarray, List, Dict]',
    y_train: 'Union[DataFrame, ndarray, List, Dict]',
    test_size: 'float' = 0.2,
    random_state: 'int' = 11
) → Tuple
```

Split Data Into Train - Test Pair. 



**Args:**
 
 - <b>`x_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  The features of the training sets. 
 - <b>`y_train`</b> (Union[pd.DataFrame, np.ndarray, List, Dict]):  The target class. 
 - <b>`test_size`</b> (float, optional):   Defaults to .2. The test size in float. 
 - <b>`random_state`</b> (int, optional):   Defaults to 11. The randomize state. 



**Returns:**
 
 - <b>`Tuple`</b>:  x_train, x_test, y_train, y_test pair. 

---

<a href="../klops/experiment/experiment.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start`

```python
start(
    classifier: 'Any',
    x_train: 'Union[ndarray, DataFrame, List[Dict]]',
    y_train: 'Union[ndarray, DataFrame, List]',
    dataset_auto_split: 'bool' = True,
    x_test: 'Union[ndarray, DataFrame, List[Dict]]' = [],
    y_test: 'Union[ndarray, DataFrame, List]' = [],
    test_size: 'float' = 0.2,
    random_state: 'int' = 11,
    tuner: 'str' = None,
    tuner_args: 'Dict' = {},
    metrices: 'Dict' = {'mean_squared_error': {}, 'root_mean_squared_error': {'squared': False}},
    **kwargs: 'Any'
) → Experiment
```

Start the experiment with given arguments. 



**Args:**
 
 - <b>`classifier`</b> (Any):  The classifier pointer class.                 Example: sklearn.naive_bayes.GaussianNB 
 - <b>`x_train`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  The input features with 2 Dimensional Array like. 
 - <b>`y_train`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  The output mapping. 
 - <b>`dataset_auto_split`</b> (bool):   Whether to automatically split the dataset into train-test pairs. 
 - <b>`x_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  The input test value. Only usable when the dataset_auto_split flag is False. 
 - <b>`y_test`</b> (Union[np.ndarray, pd.DataFrame, List[Dict]]):                  The output test value. Only usable when the dataset_auto_split flag is False. 
 - <b>`test_size`</b> (float):  The split size of the test data. 
 - <b>`random_state`</b> (int):  The number of random state. 
 - <b>`tuner`</b> (str):  The tuner could be one of (default | hyperopt | gridsearch).                 Defaults to None. 
 - <b>`tuner_args`</b> (Dict, optional):   Defaults to {}. Tunner keyworded arguments.                 A Dictionary contains key-value pairs set of hyper parameters. 
 - <b>`metrices`</b> (_type_, optional):   Defaults to                 { "mean_squared_error": {}, "root_mean_squared_error": {"squared": True}}.                 The sklearn metrices. All metrices method name could be seen here:                 https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics 



**Raises:**
 
 - <b>`ValueError`</b>:  Raised when conditions are not met. 



**Returns:**
 
 - <b>`Experiment`</b>:  The Experiment instance class. 

---

<a href="../klops/experiment/experiment.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `store_artifact`

```python
store_artifact(model: 'Any', local_path: 'str', artifact_path: 'str') → None
```

Store the artifact into a joblib file. Then upload to the artifact registry. 

**Args:**
 
 - <b>`model`</b> (Any):  The model instance. 
 - <b>`local_path`</b> (str):  The local_path to be dump. 
 - <b>`artifact_path`</b> (str):  The artifact path in cloud storage. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
