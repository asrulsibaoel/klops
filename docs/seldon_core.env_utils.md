<!-- markdownlint-disable -->

<a href="../seldon_core/env_utils#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.env_utils`
Utilities to deal with Environment variables 

**Global Variables**
---------------
- **ENV_MODEL_NAME**
- **ENV_MODEL_IMAGE**
- **ENV_SELDON_DEPLOYMENT_NAME**
- **ENV_PREDICTOR_NAME**
- **ENV_PREDICTOR_LABELS**
- **NONIMPLEMENTED_MSG**
- **NONIMPLEMENTED_IMAGE_MSG**

---

<a href="../seldon_core/env_utils/get_predictor_version#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_predictor_version`

```python
get_predictor_version(default_val: str = 'NOT_IMPLEMENTED') → str
```

Get predictor version from `ENV_PREDICTOR_LABELS` environment variable. If not set return `default_val` 



Parameters 
---------- default_val  Default value to return if the environment variable is not set 

Returns 
-------  str 


---

<a href="../seldon_core/env_utils/get_predictor_name#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_predictor_name`

```python
get_predictor_name(default_val: str = 'NOT_IMPLEMENTED') → str
```

Get predictor name from `ENV_PREDICTOR_NAME` environment variable. If not set return `default_val` 



Parameters 
---------- default_val  Default value to return if the environment variable is not set 

Returns 
-------  str 


---

<a href="../seldon_core/env_utils/get_deployment_name#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_deployment_name`

```python
get_deployment_name(default_val: str = 'NOT_IMPLEMENTED') → str
```

Get deployment name from `ENV_SELDON_DEPLOYMENT_NAME` environment variable. If not set return `default_val` 



Parameters 
---------- default_val  Default value to return if the environment variable is not set 

Returns 
-------  str 


---

<a href="../seldon_core/env_utils/get_model_name#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_model_name`

```python
get_model_name(default_val: str = 'NOT_IMPLEMENTED') → str
```

Get model name from `ENV_MODEL_NAME` environment variable. If not set return `default_val` 



Parameters 
---------- default_val  Default value to return if the environment variable is not set 

Returns 
-------  str 


---

<a href="../seldon_core/env_utils/get_image_name#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_image_name`

```python
get_image_name(default_val: str = 'NOT_IMPLEMENTED:NOT_IMPLEMENTED') → str
```

Get model image name from `ENV_MODEL_IMAGE` environment variable. If not set return `default_val` 



Parameters 
---------- default_val  Default value to return if the environment variable is not set 

Returns 
-------  str 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
