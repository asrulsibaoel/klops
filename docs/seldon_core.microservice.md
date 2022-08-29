<!-- markdownlint-disable -->

<a href="../seldon_core/microservice#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.microservice`




**Global Variables**
---------------
- **ANNOTATION_REST_TIMEOUT**
- **ANNOTATIONS_FILE**
- **DEFAULT_ANNOTATION_REST_TIMEOUT**
- **USE_MULTIPROCESS_ENV_NAME**
- **USE_MULTIPROCESS**
- **PARAMETERS_ENV_NAME**
- **HTTP_SERVICE_PORT_ENV_NAME**
- **GRPC_SERVICE_PORT_ENV_NAME**
- **METRICS_SERVICE_PORT_ENV_NAME**
- **FILTER_METRICS_ACCESS_LOGS_ENV_NAME**
- **LOG_LEVEL_ENV**
- **DEFAULT_LOG_LEVEL**
- **DEFAULT_GRPC_PORT**
- **DEFAULT_HTTP_PORT**
- **DEFAULT_METRICS_PORT**
- **DEBUG_ENV**
- **GUNICORN_ACCESS_LOG_ENV**

---

<a href="../seldon_core/microservice/start_servers#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `start_servers`

```python
start_servers(
    target1: Callable,
    target2: Callable,
    target3: Callable,
    metrics_target: Callable
) → None
```

Start servers 

Parameters 
---------- target1  Main flask process target2  Auxiliary flask process 


---

<a href="../seldon_core/microservice/parse_parameters#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `parse_parameters`

```python
parse_parameters(parameters: Dict) → Dict
```

Parse the user object parameters 

Parameters 
---------- parameters 

Returns 
------- 


---

<a href="../seldon_core/microservice/load_annotations#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_annotations`

```python
load_annotations() → Dict
```

Attempt to load annotations 

Returns 
------- 


---

<a href="../seldon_core/microservice/setup_logger#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `setup_logger`

```python
setup_logger(log_level: str, debug_mode: bool) → Logger
```






---

<a href="../seldon_core/microservice/main#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

<a href="../seldon_core/microservice/MetricsEndpointFilter#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetricsEndpointFilter`







---

<a href="../seldon_core/microservice/filter#L186"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `filter`

```python
filter(record)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
