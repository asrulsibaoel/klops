<!-- markdownlint-disable -->

<a href="../klops/seldon_core/deployment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.deployment`
Deployment Module for Seldon Core. 



---

<a href="../klops/seldon_core/deployment.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonDeployment`
_summary_ CRUD Kubernetes operation class implementation for Seldon ML Deployment. 

<a href="../klops/seldon_core/deployment.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(authentication: AbstractKubernetesAuth, namespace: str) → None
```

_summary_ The contructor for SeldonDeployment class. 

**Args:**
 
 - <b>`authentication`</b> (AbstractKubernetesAuth):  _description_  The authentication instances. Currently only supports for local cluster or GKE. 
 - <b>`namespace`</b> (str):  _description_ The kubernetes namespace deployment target. 




---

<a href="../klops/seldon_core/deployment.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_deployment_exist`

```python
check_deployment_exist(deployment_name: str) → bool
```

_summary_ Check the deployment already exists. 

**Args:**
 
 - <b>`deployment_name`</b> (str):  _description_ The deployment name, Example: iris-model 

**Returns:**
 
 - <b>`bool`</b>:  _description_ The deployment existence. 

**Raises:**
 
 - <b>`AttributeError`</b>:  _description_ Raised when the key doesn't exists. 
 - <b>`NoneTypeException`</b>:  _description_ Raised when wrong compared with None Object. 

---

<a href="../klops/seldon_core/deployment.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect_to_cluster`

```python
connect_to_cluster() → None
```

_summary_ Connect to the kubernetes cluster given from the constructor arguments. 

---

<a href="../klops/seldon_core/deployment.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(deployment_config: Dict) → bool
```

_summary_ Deploy the ML Model 

**Args:**
 
 - <b>`deployment_config`</b> (Union[object, Dict]):  _description_  Deployment Configuration Object. 

**Returns:**
 
 - <b>`bool`</b>:  _description_ Boolean result of deployment deletion. 

**Raises:**
 
 - <b>`SeldonDeploymentException`</b>:  _description_ Raised when the deployment failed. 

---

<a href="../klops/seldon_core/deployment.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deploy`

```python
deploy(deployment_config: Dict) → Dict
```

_description_ Deploy the ML Model 

**Args:**
 
 - <b>`deployment_config`</b> (Union[object, Dict]):  _description_  Deployment Configuration Object. 

**Returns:**
 
 - <b>`deployment_result`</b> (Dict):  _description_ The deployment result metadata in a dictionary. 

**Raises:**
 
 - <b>`SeldonDeploymentException`</b>:  _description_ Raised when the deployment failed. 

---

<a href="../klops/seldon_core/deployment.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load_deployment_configuration`

```python
load_deployment_configuration(file_name: str)
```

_summary_ Load the deployment configuration file into a Python dictionary. 

**Args:**
 
 - <b>`file_name`</b> (str):  _description_ The deployment file name.  It can be Yaml file (.yml or .yaml) or JSON file. 

**Returns:**
 
 - <b>`deployment_config`</b> (dict):  _description_ Seldon Deployment configuration dictionary. 

**Raises:**
 
 - <b>`ValueError`</b>:  _description_ When the file type are not yaml or json. 
 - <b>`JSONDecodeError`</b>:  _description_ When the JSON file contains wrong format. 
 - <b>`YAMLError`</b>:  _description_ When the Yaml contains wrong format. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
