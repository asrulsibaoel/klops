<!-- markdownlint-disable -->

<a href="../seldon_core/wrapper#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.wrapper`




**Global Variables**
---------------
- **ANNOTATION_GRPC_MAX_MSG_SIZE**
- **PRED_UNIT_ID**
- **METRICS_ENDPOINT**
- **PAYLOAD_PASSTHROUGH**

---

<a href="../seldon_core/wrapper/get_rest_microservice#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_rest_microservice`

```python
get_rest_microservice(user_model, seldon_metrics)
```






---

<a href="../seldon_core/wrapper/get_metrics_microservice#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_metrics_microservice`

```python
get_metrics_microservice(seldon_metrics)
```






---

<a href="../seldon_core/wrapper/get_grpc_server#L282"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_grpc_server`

```python
get_grpc_server(
    user_model,
    seldon_metrics,
    annotations={},
    trace_interceptor=None,
    num_threads=1
)
```






---

<a href="../seldon_core/wrapper/SeldonModelGRPC#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonModelGRPC`




<a href="../seldon_core/wrapper/__init__#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(user_model, seldon_metrics)
```








---

<a href="../seldon_core/wrapper/Aggregate#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Aggregate`

```python
Aggregate(request_grpc, context)
```





---

<a href="../seldon_core/wrapper/GraphMetadata#L277"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `GraphMetadata`

```python
GraphMetadata(request_grpc, context)
```

GraphMetadata method of rpc Seldon service 

---

<a href="../seldon_core/wrapper/Metadata#L269"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Metadata`

```python
Metadata(request_grpc, context)
```

Metadata method of rpc Model service 

---

<a href="../seldon_core/wrapper/ModelMetadata#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ModelMetadata`

```python
ModelMetadata(request_grpc, context)
```

ModelMetadata method of rpc Seldon service 

---

<a href="../seldon_core/wrapper/Predict#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Predict`

```python
Predict(request_grpc, context)
```





---

<a href="../seldon_core/wrapper/Route#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Route`

```python
Route(request_grpc, context)
```





---

<a href="../seldon_core/wrapper/SendFeedback#L244"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(feedback_grpc, context)
```





---

<a href="../seldon_core/wrapper/TransformInput#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformInput`

```python
TransformInput(request_grpc, context)
```





---

<a href="../seldon_core/wrapper/TransformOutput#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformOutput`

```python
TransformOutput(request_grpc, context)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
