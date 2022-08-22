<!-- markdownlint-disable -->

<a href="../klops/seldon_core/deployment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.deployment`
Deployment Module for Seldon Core. 



---

<a href="../klops/seldon_core/deployment.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonDeployment`
CRUD Kubernetes operation class implementation for Seldon ML Deployment. 

<a href="../klops/seldon_core/deployment.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(authentication: AbstractKubernetesAuth, namespace: str) → None
```








---

<a href="../klops/seldon_core/deployment.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_deployment_exist`

```python
check_deployment_exist(deployment_name: str) → bool
```

Check the deployment already exists. 

**Args:**
 
 - <b>`deployment_name`</b> (str):  The deployment name, Example: iris-model 

**Returns:**
 
 - <b>`bool`</b>:  The deployment existence. 

**Raises:**
 
 - <b>`AttributeError`</b>:  Raised when the key doesn't exists. 
 - <b>`NoneTypeException`</b>:  Raised when wrong compared with None Object. 

---

<a href="../klops/seldon_core/deployment.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect_to_cluster`

```python
connect_to_cluster() → None
```

connect_to_cluster. 

**Args:**
  cluster_name (str):  String of cluster name. 

**Raises:**
 
 - <b>`Exception`</b>:  fff. 

---

<a href="../klops/seldon_core/deployment.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(deployment_config: Dict) → bool
```

Deploy the ML Model 

**Args:**
  deployment_config (Union[object, Dict]):  Deployment Configuration Object. 

**Returns:**
 
 - <b>`bool`</b>:  Boolean result of deployment deletion. 

**Raises:**
 
 - <b>`SeldonDeploymentException`</b>:  Raised when the deployment failed. 

---

<a href="../klops/seldon_core/deployment.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deploy`

```python
deploy(deployment_config: Dict) → Dict
```

Deploy the ML Model 

**Args:**
  deployment_config (Union[object, Dict]):  Deployment Configuration Object. 

**Returns:**
 
 - <b>`deployment_result`</b> (Dict):  The deployment result metadata in a dictionary. 

**Raises:**
 
 - <b>`SeldonDeploymentException`</b>:  Raised when the deployment failed. 

---

<a href="../klops/seldon_core/deployment.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load_deployment_configuration`

```python
load_deployment_configuration(file_name: str)
```

Load the deployment configuration file into a Python dictionary. 

**Args:**
 
 - <b>`file_name`</b> (str):  the deployment file name.  It can be Yaml file (.yml or .yaml) or JSON file. 

**Returns:**
 
 - <b>`deployment_config`</b> (dict):  Seldon Deployment configuration dictionary. 

**Raises:**
 
 - <b>`ValueError`</b>:  When the file type are not yaml or json. 
 - <b>`JSONDecodeError`</b>:  When the JSON file contains wrong format. 
 - <b>`YAMLError`</b>:  When the Yaml contains wrong format. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
