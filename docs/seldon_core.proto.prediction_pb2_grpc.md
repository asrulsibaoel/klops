<!-- markdownlint-disable -->

<a href="../seldon_core/proto/prediction_pb2_grpc#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.proto.prediction_pb2_grpc`
Client and server classes corresponding to protobuf-defined services. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_GenericServicer_to_server#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_GenericServicer_to_server`

```python
add_GenericServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_ModelServicer_to_server#L262"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_ModelServicer_to_server`

```python
add_ModelServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_RouterServicer_to_server#L378"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_RouterServicer_to_server`

```python
add_RouterServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_TransformerServicer_to_server#L461"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_TransformerServicer_to_server`

```python
add_TransformerServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_OutputTransformerServicer_to_server#L522"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_OutputTransformerServicer_to_server`

```python
add_OutputTransformerServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_CombinerServicer_to_server#L583"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_CombinerServicer_to_server`

```python
add_CombinerServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/add_SeldonServicer_to_server#L677"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_SeldonServicer_to_server`

```python
add_SeldonServicer_to_server(servicer, server)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/GenericStub#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GenericStub`
[END Messages] 

[START Services] 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/GenericServicer#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GenericServicer`
[END Messages] 

[START Services] 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Aggregate#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Aggregate`

```python
Aggregate(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/Route#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Route`

```python
Route(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformInput#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformInput`

```python
TransformInput(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformOutput#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformOutput`

```python
TransformOutput(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Generic#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Generic`
[END Messages] 

[START Services] 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Aggregate#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Aggregate`

```python
Aggregate(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/Route#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Route`

```python
Route(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L196"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformInput#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformInput`

```python
TransformInput(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformOutput#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformOutput`

```python
TransformOutput(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/ModelStub#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ModelStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/ModelServicer#L240"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ModelServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Metadata#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Metadata`

```python
Metadata(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/Predict#L243"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Predict`

```python
Predict(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Model#L286"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Model`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Metadata#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Metadata`

```python
Metadata(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/Predict#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Predict`

```python
Predict(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L306"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/RouterStub#L341"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RouterStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L344"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/RouterServicer#L362"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RouterServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Route#L365"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Route`

```python
Route(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L371"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Router#L397"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Router`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Route#L400"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Route`

```python
Route(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L417"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformerStub#L435"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TransformerStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L438"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformerServicer#L451"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TransformerServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformInput#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformInput`

```python
TransformInput(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Transformer#L475"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Transformer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformInput#L478"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformInput`

```python
TransformInput(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/OutputTransformerStub#L496"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `OutputTransformerStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L499"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/OutputTransformerServicer#L512"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `OutputTransformerServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformOutput#L515"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformOutput`

```python
TransformOutput(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/OutputTransformer#L536"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `OutputTransformer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/TransformOutput#L539"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `TransformOutput`

```python
TransformOutput(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/CombinerStub#L557"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CombinerStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L560"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/CombinerServicer#L573"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CombinerServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Aggregate#L576"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Aggregate`

```python
Aggregate(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Combiner#L597"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Combiner`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/Aggregate#L600"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Aggregate`

```python
Aggregate(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```






---

<a href="../seldon_core/proto/prediction_pb2_grpc/SeldonStub#L618"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonStub`
Missing associated documentation comment in .proto file. 

<a href="../seldon_core/proto/prediction_pb2_grpc/__init__#L621"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(channel)
```

Constructor. 



**Args:**
 
 - <b>`channel`</b>:  A grpc.Channel. 





---

<a href="../seldon_core/proto/prediction_pb2_grpc/SeldonServicer#L649"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonServicer`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/GraphMetadata#L670"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `GraphMetadata`

```python
GraphMetadata(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/ModelMetadata#L664"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ModelMetadata`

```python
ModelMetadata(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/Predict#L652"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Predict`

```python
Predict(request, context)
```

Missing associated documentation comment in .proto file. 

---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L658"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(request, context)
```

Missing associated documentation comment in .proto file. 


---

<a href="../seldon_core/proto/prediction_pb2_grpc/Seldon#L706"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Seldon`
Missing associated documentation comment in .proto file. 




---

<a href="../seldon_core/proto/prediction_pb2_grpc/GraphMetadata#L760"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `GraphMetadata`

```python
GraphMetadata(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/ModelMetadata#L743"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ModelMetadata`

```python
ModelMetadata(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/Predict#L709"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Predict`

```python
Predict(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```





---

<a href="../seldon_core/proto/prediction_pb2_grpc/SendFeedback#L726"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SendFeedback`

```python
SendFeedback(
    request,
    target,
    options=(),
    channel_credentials=None,
    call_credentials=None,
    insecure=False,
    compression=None,
    wait_for_ready=None,
    timeout=None,
    metadata=None
)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
