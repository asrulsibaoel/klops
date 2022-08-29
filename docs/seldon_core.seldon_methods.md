<!-- markdownlint-disable -->

<a href="../seldon_core/seldon_methods#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.seldon_methods`




**Global Variables**
---------------
- **AGGREGATE_METRIC_METHOD_TAG**
- **FEEDBACK_METRIC_METHOD_TAG**
- **HEALTH_METRIC_METHOD_TAG**
- **INPUT_TRANSFORM_METRIC_METHOD_TAG**
- **OUTPUT_TRANSFORM_METRIC_METHOD_TAG**
- **PREDICT_METRIC_METHOD_TAG**
- **ROUTER_METRIC_METHOD_TAG**
- **INCLUDE_METRICS_IN_CLIENT_RESPONSE**

---

<a href="../seldon_core/seldon_methods/handle_raw_custom_metrics#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `handle_raw_custom_metrics`

```python
handle_raw_custom_metrics(
    msg: Union[SeldonMessage, Dict],
    seldon_metrics: SeldonMetrics,
    is_proto: bool,
    method: str
)
```

Update SeldonMetrics object with custom metrics from raw methods. If INCLUDE_METRICS_IN_CLIENT_RESPONSE environmental variable is set to "true" metrics will be dropped from msg. 


---

<a href="../seldon_core/seldon_methods/predict#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `predict`

```python
predict(
    user_model: Any,
    request: Union[SeldonMessage, List, Dict, bytes],
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict, bytes]
```

Call the user model to get a prediction and package the response 

Parameters 
---------- user_model  User defined class instance request  The incoming request 

Returns 
-------  The prediction 


---

<a href="../seldon_core/seldon_methods/send_feedback#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `send_feedback`

```python
send_feedback(
    user_model: Any,
    request: Feedback,
    predictive_unit_id: str,
    seldon_metrics: SeldonMetrics
) → SeldonMessage
```

Parameters 
---------- user_model  A Seldon user model request  SeldonMesage proto predictive_unit_id  The ID of the enclosing container predictive unit. Will be taken from environment. 

Returns 
------- 


---

<a href="../seldon_core/seldon_methods/transform_input#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `transform_input`

```python
transform_input(
    user_model: Any,
    request: Union[SeldonMessage, List, Dict],
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict]
```

Parameters 
---------- user_model  User defined class to handle transform input request  The incoming request 

Returns 
-------  The transformed request 


---

<a href="../seldon_core/seldon_methods/transform_output#L328"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `transform_output`

```python
transform_output(
    user_model: Any,
    request: Union[SeldonMessage, List, Dict],
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict]
```

Parameters 
---------- user_model  User defined class to handle transform input request  The incoming request 

Returns 
-------  The transformed request 


---

<a href="../seldon_core/seldon_methods/route#L422"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `route`

```python
route(
    user_model: Any,
    request: Union[SeldonMessage, List, Dict],
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict]
```

Parameters 
---------- user_model  A Seldon user model request  A SelodonMessage proto seldon_metrics  A SeldonMetrics instance Returns 
------- 


---

<a href="../seldon_core/seldon_methods/aggregate#L513"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `aggregate`

```python
aggregate(
    user_model: Any,
    request: Union[SeldonMessageList, List, Dict],
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict]
```

Aggregate a list of payloads 

Parameters 
---------- user_model  A Seldon user model request  SeldonMessage proto seldon_metrics  A SeldonMetrics instance 

Returns 
-------  Aggregated SeldonMessage proto 


---

<a href="../seldon_core/seldon_methods/health_status#L644"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `health_status`

```python
health_status(
    user_model: Any,
    seldon_metrics: SeldonMetrics
) → Union[SeldonMessage, List, Dict]
```

Call the user model to check the health of the model 

Parameters 
---------- user_model  User defined class instance seldon_metrics  A SeldonMetrics instance 

Returns 
-------  Health check output 


---

<a href="../seldon_core/seldon_methods/init_metadata#L678"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `init_metadata`

```python
init_metadata(user_model: Any) → Dict
```

Call the user model to get the model init_metadata 

Parameters 
---------- user_model  User defined class instance 

Returns 
-------  Validated model metadata 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
