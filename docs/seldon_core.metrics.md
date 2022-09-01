<!-- markdownlint-disable -->

<a href="../seldon_core/metrics#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.metrics`




**Global Variables**
---------------
- **FEEDBACK_KEY**
- **FEEDBACK_REWARD_KEY**
- **COUNTER**
- **GAUGE**
- **TIMER**
- **BINS**
- **image**
- **model_image**
- **model_version**
- **predictor_version**
- **legacy_mode**
- **DEFAULT_LABELS**
- **FEEDBACK_METRIC_METHOD_TAG**
- **PREDICT_METRIC_METHOD_TAG**
- **INPUT_TRANSFORM_METRIC_METHOD_TAG**
- **OUTPUT_TRANSFORM_METRIC_METHOD_TAG**
- **ROUTER_METRIC_METHOD_TAG**
- **AGGREGATE_METRIC_METHOD_TAG**
- **HEALTH_METRIC_METHOD_TAG**

---

<a href="../seldon_core/metrics/split_image_tag#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `split_image_tag`

```python
split_image_tag(tag: str) → Tuple[str]
```

Extract image name and version from an image tag. 

Parameters 
---------- tag  Fully qualified docker image tag. Eg. seldonio/sklearn-iris:0.1 

Returns 
-------  Image name, image version tuple 


---

<a href="../seldon_core/metrics/create_counter#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_counter`

```python
create_counter(key: str, value: float)
```

Utility method to create a counter metric Parameters 
---------- key  Counter name value  Counter value 

Returns 
-------  Valid counter metric dict 


---

<a href="../seldon_core/metrics/create_gauge#L252"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_gauge`

```python
create_gauge(key: str, value: float) → Dict
```

Utility method to create a gauge metric Parameters 
---------- key  Gauge name value  Gauge value 

Returns 
-------  Valid Gauge metric dict 


---

<a href="../seldon_core/metrics/create_timer#L271"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_timer`

```python
create_timer(key: str, value: float) → Dict
```

Utility mehtod to create a timer metric Parameters 
---------- key  Name of metric value  Value for metric 

Returns 
-------  Valid timer metric dict 


---

<a href="../seldon_core/metrics/validate_metrics#L290"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `validate_metrics`

```python
validate_metrics(metrics: List[Dict]) → bool
```

Validate a list of metrics Parameters 
---------- metrics  List of metrics 

Returns 
------- 


---

<a href="../seldon_core/metrics/SeldonMetrics#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonMetrics`
Class to manage custom metrics stored in shared memory. 

<a href="../seldon_core/metrics/__init__#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(worker_id_func=<built-in function getpid>, extra_default_labels={})
```








---

<a href="../seldon_core/metrics/clear#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear`

```python
clear()
```

Clear all metrics from current worker. 

---

<a href="../seldon_core/metrics/collect#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `collect`

```python
collect()
```





---

<a href="../seldon_core/metrics/generate_metrics#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_metrics`

```python
generate_metrics()
```





---

<a href="../seldon_core/metrics/update#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(custom_metrics: List[Dict], method: str)
```





---

<a href="../seldon_core/metrics/update_reward#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_reward`

```python
update_reward(reward: float)
```

Update metrics key corresponding to feedback reward counter. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
