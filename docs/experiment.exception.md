<!-- markdownlint-disable -->

<a href="../klops/experiment/exception.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `experiment.exception`
Experiment exception module. 

Put all the exception handlers here. 



---

<a href="../klops/experiment/exception.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ExperimentFailedException`
Experiment Failed Exception 

Raised when the experiment got failed. 

<a href="../klops/experiment/exception.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message: str, *args: object) → None
```

The Experiment Failed Constructor 

Message would store the root causes. 

**Args:**
 
 - <b>`message`</b> (str):  _description_ 





---

<a href="../klops/experiment/exception.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `InvalidArgumentsException`
Invalid Arguments Passed 

Raised when the given arguments are invalid. 

<a href="../klops/experiment/exception.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message: str, *args: object) → None
```

The Exception Constructor 



**Args:**
 
 - <b>`message`</b> (str):  message that would be displayed to the user. 





---

<a href="../klops/experiment/exception.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `LogMetricException`
Log Metric Exception 

Raised when the Logging the metrics are failed. 

<a href="../klops/experiment/exception.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message: str, *args: object) → None
```

The Log Metric Exception Constructor 

Message would store the root causes. 

**Args:**
 
 - <b>`message`</b> (str):  _description_ 





---

<a href="../klops/experiment/exception.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UnknownExperimentTunerTypeException`
Unknown Experiment Tunner Exception 

Raised when the tuner is not one of `default` | `gridsearch` | `hyperopt`. 

<a href="../klops/experiment/exception.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message, *args: object) → None
```

The Exception Constructor. 



**Args:**
 
 - <b>`message`</b> (_type_):  The Exception message would be displayed. 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
