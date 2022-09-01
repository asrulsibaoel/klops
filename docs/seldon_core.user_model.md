<!-- markdownlint-disable -->

<a href="../seldon_core/user_model#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.user_model`




**Global Variables**
---------------
- **INCLUDE_METRICS_IN_CLIENT_RESPONSE**

---

<a href="../seldon_core/user_model/client_custom_tags#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_custom_tags`

```python
client_custom_tags(user_model: SeldonComponent) → Dict
```

Get tags from user model 

Parameters 
---------- user_model 

Returns 
-------  Dictionary of key value pairs 


---

<a href="../seldon_core/user_model/client_class_names#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_class_names`

```python
client_class_names(
    user_model: SeldonComponent,
    predictions: ndarray
) → Iterable[str]
```

Get class names from user model 

Parameters 
---------- user_model  User defined class instance predictions  Prediction results Returns 
-------  Class names 


---

<a href="../seldon_core/user_model/client_predict#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_predict`

```python
client_predict(
    user_model: SeldonComponent,
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    **kwargs: Dict
) → SeldonResponse
```

Get prediction from user model 

Parameters 
---------- user_model  A seldon user model features  The data payload feature_names  The feature names in the payload kwargs  Optional keyword arguments Returns 
-------  A prediction from the user model 


---

<a href="../seldon_core/user_model/client_transform_input#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_transform_input`

```python
client_transform_input(
    user_model: SeldonComponent,
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    **kwargs: Dict
) → SeldonResponse
```

Transform data with user model 

Parameters 
---------- user_model  A Seldon user model features  Data payload feature_names  Data payload column names kwargs  Optional keyword args 

Returns 
-------  Transformed data 


---

<a href="../seldon_core/user_model/client_transform_output#L287"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_transform_output`

```python
client_transform_output(
    user_model: SeldonComponent,
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    **kwargs: Dict
) → SeldonResponse
```

Transform output 

Parameters 
---------- user_model  A Seldon user model features  Data payload feature_names  Data payload column names kwargs  Optional keyword args Returns 
-------  Transformed data 


---

<a href="../seldon_core/user_model/client_custom_metrics#L326"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_custom_metrics`

```python
client_custom_metrics(
    user_model: SeldonComponent,
    seldon_metrics: SeldonMetrics,
    method: str,
    runtime_metrics: List[Dict] = []
) → List[Dict]
```

Get custom metrics for client and update SeldonMetrics. 

This function will return empty list if INCLUDE_METRICS_IN_CLIENT_RESPONSE environmental variable is NOT set to "true" or "True". 

Parameters 
---------- user_model  A Seldon user model seldon_metrics  A SeldonMetrics instance method:  tag of a method that collected the metrics runtime_metrics:  metrics that were defined on runtime Returns 
-------  A list of custom metrics 


---

<a href="../seldon_core/user_model/client_feature_names#L385"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_feature_names`

```python
client_feature_names(
    user_model: SeldonComponent,
    original: Iterable[str]
) → Iterable[str]
```

Get feature names for user model 

Parameters 
---------- user_model  A Seldon user model original  Original feature names Returns 
-------  A list if feature names 


---

<a href="../seldon_core/user_model/client_send_feedback#L410"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_send_feedback`

```python
client_send_feedback(
    user_model: SeldonComponent,
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    reward: float,
    truth: Union[ndarray, str, bytes],
    routing: Optional[int]
) → SeldonResponse
```

Feedback to user model 

Parameters 
---------- user_model  A Seldon user model features  A payload feature_names  Payload column names reward  Reward truth  True outcome routing  Optional routing 

Returns 
-------  Optional payload 


---

<a href="../seldon_core/user_model/client_route#L453"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_route`

```python
client_route(
    user_model: SeldonComponent,
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    **kwargs: Dict
) → SeldonResponse
```

Get routing from user model 

Parameters 
---------- user_model  A Seldon user model features  Payload feature_names  Columns for payload 

Returns 
-------  Routing index for one of children 


---

<a href="../seldon_core/user_model/client_aggregate#L485"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_aggregate`

```python
client_aggregate(
    user_model: SeldonComponent,
    features_list: List[Union[ndarray, str, bytes]],
    feature_names_list: List
) → SeldonResponse
```

Aggregate payloads 

Parameters 
---------- user_model  A Seldon user model features_list  A list of payloads feature_names_list  Column names for payloads Returns 
-------  An aggregated payload 


---

<a href="../seldon_core/user_model/client_health_status#L512"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `client_health_status`

```python
client_health_status(
    user_model: SeldonComponent
) → Union[ndarray, List, str, bytes]
```

Perform a health check 

Parameters 
---------- user_model  A Seldon user model Returns 
-------  Health check results 


---

<a href="../seldon_core/user_model/SeldonNotImplementedError#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonNotImplementedError`




<a href="../seldon_core/user_model/__init__#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message)
```









---

<a href="../seldon_core/user_model/SeldonResponse#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonResponse`
SeldonResponse 

Simple class to store data returned by SeldonComponent methods together with relevant runtime metrics and runtime request tags. 

<a href="../seldon_core/user_model/__init__#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    data: Union[ndarray, List, str, bytes],
    tags: Dict = None,
    metrics: List[Dict] = None
)
```








---

<a href="../seldon_core/user_model/create#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    data: Union[ndarray, List, Dict, str, bytes, ForwardRef('SeldonResponse')]
) → SeldonResponse
```






---

<a href="../seldon_core/user_model/SeldonComponent#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonComponent`




<a href="../seldon_core/user_model/__init__#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(**kwargs)
```








---

<a href="../seldon_core/user_model/aggregate#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `aggregate`

```python
aggregate(
    features_list: List[Union[ndarray, str, bytes]],
    feature_names_list: List
) → Union[ndarray, List, Dict, str, bytes, SeldonResponse]
```





---

<a href="../seldon_core/user_model/aggregate_raw#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `aggregate_raw`

```python
aggregate_raw(msgs: SeldonMessageList) → Union[SeldonMessage, Dict]
```





---

<a href="../seldon_core/user_model/class_names#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `class_names`

```python
class_names() → Iterable[str]
```





---

<a href="../seldon_core/user_model/feature_names#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `feature_names`

```python
feature_names() → Iterable[str]
```





---

<a href="../seldon_core/user_model/health_status#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `health_status`

```python
health_status() → Union[ndarray, List, str, bytes]
```





---

<a href="../seldon_core/user_model/health_status_raw#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `health_status_raw`

```python
health_status_raw() → SeldonMessage
```





---

<a href="../seldon_core/user_model/init_metadata#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init_metadata`

```python
init_metadata() → Dict
```





---

<a href="../seldon_core/user_model/load#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load`

```python
load()
```





---

<a href="../seldon_core/user_model/metadata#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `metadata`

```python
metadata() → Dict
```





---

<a href="../seldon_core/user_model/metrics#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `metrics`

```python
metrics() → List[Dict]
```





---

<a href="../seldon_core/user_model/predict#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `predict`

```python
predict(
    X: ndarray,
    names: Iterable[str],
    meta: Dict = None
) → Union[ndarray, List, Dict, str, bytes, SeldonResponse]
```





---

<a href="../seldon_core/user_model/predict_raw#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `predict_raw`

```python
predict_raw(msg: SeldonMessage) → Union[SeldonMessage, Dict]
```





---

<a href="../seldon_core/user_model/route#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `route`

```python
route(
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str]
) → Union[int, SeldonResponse]
```





---

<a href="../seldon_core/user_model/route_raw#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `route_raw`

```python
route_raw(msg: SeldonMessage) → Union[SeldonMessage, Dict]
```





---

<a href="../seldon_core/user_model/send_feedback#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_feedback`

```python
send_feedback(
    features: Union[ndarray, str, bytes],
    feature_names: Iterable[str],
    reward: float,
    truth: Union[ndarray, str, bytes],
    routing: Optional[int]
) → Union[ndarray, List, Dict, str, bytes, NoneType, SeldonResponse]
```





---

<a href="../seldon_core/user_model/send_feedback_raw#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_feedback_raw`

```python
send_feedback_raw(feedback: Feedback) → Union[SeldonMessage, Dict]
```





---

<a href="../seldon_core/user_model/tags#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `tags`

```python
tags() → Dict
```





---

<a href="../seldon_core/user_model/transform_input#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `transform_input`

```python
transform_input(
    X: ndarray,
    names: Iterable[str],
    meta: Dict = None
) → Union[ndarray, List, Dict, str, bytes, SeldonResponse]
```





---

<a href="../seldon_core/user_model/transform_input_raw#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `transform_input_raw`

```python
transform_input_raw(msg: SeldonMessage) → Union[SeldonMessage, Dict]
```





---

<a href="../seldon_core/user_model/transform_output#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `transform_output`

```python
transform_output(
    X: ndarray,
    names: Iterable[str],
    meta: Dict = None
) → Union[ndarray, List, Dict, str, bytes, SeldonResponse]
```





---

<a href="../seldon_core/user_model/transform_output_raw#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `transform_output_raw`

```python
transform_output_raw(msg: SeldonMessage) → Union[SeldonMessage, Dict]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
