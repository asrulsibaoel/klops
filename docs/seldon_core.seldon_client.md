<!-- markdownlint-disable -->

<a href="../seldon_core/seldon_client#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.seldon_client`





---

<a href="../seldon_core/seldon_client/microservice_api_rest_seldon_message#L789"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_rest_seldon_message`

```python
microservice_api_rest_seldon_message(
    method: str = 'predict',
    microservice_endpoint: str = 'localhost:5000',
    shape: Tuple = (1, 1),
    data: object = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    names: Iterable[str] = None,
    **kwargs
) → SeldonClientPrediction
```

Call Seldon microservice REST API 

Parameters 
---------- method  The microservice method to call microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes method  The microservice method to call shape  The shape of the data to send namespace  k8s namespace of running deployment shape  Shape of the data to send data  Numpy array data to send payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data payload str_data  String data payload json_data  JSON data payload names  Column names kwargs 

Returns 
-------  A SeldonClientPrediction data response 


---

<a href="../seldon_core/seldon_client/microservice_api_rest_aggregate#L869"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_rest_aggregate`

```python
microservice_api_rest_aggregate(
    microservice_endpoint: str = 'localhost:5000',
    shape: Tuple = (1, 1),
    datas: List[ndarray] = None,
    ndatas: int = None,
    payload_type: str = 'tensor',
    names: Iterable[str] = None,
    **kwargs
) → SeldonClientCombine
```

Call Seldon microservice REST API aggregate endpoint 

Parameters 
---------- microservice_endpoint  Running microservice endpoint shape  The shape of the data to send datas  List of Numpy array data to send ndatas  Multiple numpy arrays to send for aggregation payload_type  payload - tensor, ndarray or tftensor names  Column names kwargs 

Returns 
-------  A SeldonClientPrediction 


---

<a href="../seldon_core/seldon_client/microservice_api_rest_feedback#L935"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_rest_feedback`

```python
microservice_api_rest_feedback(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    reward: float = 0,
    microservice_endpoint: str = None,
    **kwargs
) → SeldonClientFeedback
```

Call Seldon microserice REST API to send feedback 

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback microservice_endpoint  Running microservice endpoint kwargs 

Returns 
-------  A SeldonClientFeedback 


---

<a href="../seldon_core/seldon_client/microservice_api_grpc_seldon_message#L982"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_grpc_seldon_message`

```python
microservice_api_grpc_seldon_message(
    method: str = 'predict',
    microservice_endpoint: str = 'localhost:5000',
    shape: Tuple = (1, 1),
    data: object = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    custom_data: Any = None,
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    names: Iterable[str] = None,
    **kwargs
) → SeldonClientPrediction
```

Call Seldon microservice gRPC API 

Parameters 
---------- method  Method to call microservice_endpoint  Running microservice endpoint shape  The shape of the data to send data  Numpy array data to send payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send custom_data  Custom data to send grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes names  column names kwargs 

Returns 
-------  SeldonClientPrediction 


---

<a href="../seldon_core/seldon_client/microservice_api_grpc_aggregate#L1075"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_grpc_aggregate`

```python
microservice_api_grpc_aggregate(
    microservice_endpoint: str = 'localhost:5000',
    shape: Tuple = (1, 1),
    datas: List[ndarray] = None,
    ndatas: int = None,
    payload_type: str = 'tensor',
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    names: Iterable[str] = None,
    **kwargs
) → SeldonClientCombine
```

Call Seldon microservice gRPC API aggregate 

Parameters 
---------- microservice_endpoint  Microservice API endpoint shape  Shape of the data to send datas  List of Numpy array data to send ndatas  Multiple numpy arrays to send for aggregation payload_type  payload - tensor, ndarray or tftensor grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes names  Column names kwargs 

Returns 
-------  SeldonClientCombine 


---

<a href="../seldon_core/seldon_client/microservice_api_grpc_feedback#L1147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `microservice_api_grpc_feedback`

```python
microservice_api_grpc_feedback(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    reward: float = 0,
    microservice_endpoint: str = None,
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    **kwargs
) → SeldonClientFeedback
```

Call Seldon gRPC 

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback microservice_endpoint  Running microservice endpoint kwargs 

Returns 
------- 


---

<a href="../seldon_core/seldon_client/rest_predict_seldon#L1199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rest_predict_seldon`

```python
rest_predict_seldon(
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8002',
    shape: Tuple = (1, 1),
    data: object = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    names: Iterable[str] = None,
    client_return_type: str = 'proto',
    raw_data: Dict = None,
    meta: Dict = {},
    **kwargs
) → SeldonClientPrediction
```

Call Seldon API Gateway using REST 

Parameters 
---------- namespace  k8s namespace of running deployment shape  Shape of endpoint data  Data to send payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send names  column names client_return_type  the return type of all functions can be either dict or proto raw_data  Raw payload (dictionary) given by the user meta  Custom meta data map, supplied as tags kwargs 

Returns 
-------  Seldon Client Prediction 


---

<a href="../seldon_core/seldon_client/grpc_predict_seldon#L1295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grpc_predict_seldon`

```python
grpc_predict_seldon(
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8004',
    shape: Tuple[int, int] = (1, 1),
    data: ndarray = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    custom_data: Any = None,
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    names: Iterable[str] = None,
    client_return_type: str = 'proto',
    raw_data: Dict = None,
    **kwargs
) → SeldonClientPrediction
```

Call Seldon gRPC API Gateway endpoint 

Parameters 
---------- namespace  k8s namespace of running deployment shape  Shape of endpoint data  Data to send payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send custom_data  Custom data to send grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes names  Column names client_return_type  the return type of all functions can be either dict or proto raw_data  Raw payload (dictionary or proto) given by the user kwargs 

Returns 
-------  A SeldonMessage proto 


---

<a href="../seldon_core/seldon_client/rest_predict_gateway#L1391"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rest_predict_gateway`

```python
rest_predict_gateway(
    deployment_name: str,
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8003',
    shape: Tuple[int, int] = (1, 1),
    data: ndarray = None,
    headers: Dict = None,
    gateway_prefix: str = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, Dict, List] = None,
    names: Iterable[str] = None,
    call_credentials: SeldonCallCredentials = None,
    channel_credentials: SeldonChannelCredentials = None,
    http_path: str = None,
    meta: Dict = {},
    client_return_type: str = 'proto',
    raw_data: Dict = None,
    ssl: bool = None,
    **kwargs
) → SeldonClientPrediction
```

REST request to Gateway Ingress 

Parameters 
---------- deployment_name  The name of the Seldon Deployment namespace  k8s namespace of running deployment gateway_endpoint  The host:port of gateway shape  The shape of the data to send data  The numpy data to send headers  Headers to add to request gateway_prefix  The prefix path to add to the request payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send as str, dict or list names  Column names call_credentials  Call credentials - see SeldonCallCredentials channel_credentials  Channel credentials - see SeldonChannelCredentials http_path  Custom http path meta  Custom meta map client_return_type  the return type of all functions can be either dict or proto raw_data  Raw payload (dictionary) given by the user 

Returns 
-------  A requests Response object 


---

<a href="../seldon_core/seldon_client/explain_predict_gateway#L1574"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `explain_predict_gateway`

```python
explain_predict_gateway(
    deployment_name: str,
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8003',
    gateway: str = None,
    transport: str = 'rest',
    shape: Tuple[int, int] = (1, 1),
    data: ndarray = None,
    headers: Dict = None,
    gateway_prefix: str = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    names: Iterable[str] = None,
    call_credentials: SeldonCallCredentials = None,
    channel_credentials: SeldonChannelCredentials = None,
    http_path: str = None,
    client_return_type: str = 'dict',
    predictor: str = None,
    ssl: bool = None,
    **kwargs
) → SeldonClientPrediction
```

REST explain request to Gateway Ingress 

Parameters 
---------- deployment_name  The name of the Seldon Deployment namespace  k8s namespace of running deployment gateway_endpoint  The host:port of gateway gateway  The type of gateway which can be seldon or ambassador/istio transport  The type of transport, in this case only rest is supported shape  The shape of the data to send data  The numpy data to send headers  Headers to add to request gateway_prefix  The prefix path to add to the request payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send names  Column names call_credentials  Call credentials - see SeldonCallCredentials channel_credentials  Channel credentials - see SeldonChannelCredentials http_path  Custom http path client_return_type  the return type of all functions can be either dict or proto 

Returns 
-------  A JSON Dict 


---

<a href="../seldon_core/seldon_client/grpc_predict_gateway#L1756"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grpc_predict_gateway`

```python
grpc_predict_gateway(
    deployment_name: str,
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8003',
    shape: Tuple[int, int] = (1, 1),
    data: ndarray = None,
    headers: Dict = None,
    payload_type: str = 'tensor',
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    custom_data: Any = None,
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    names: Iterable[str] = None,
    call_credentials: SeldonCallCredentials = None,
    channel_credentials: SeldonChannelCredentials = None,
    meta: Dict = {},
    client_return_type: str = 'proto',
    raw_data: Dict = None,
    ssl: bool = None,
    **kwargs
) → SeldonClientPrediction
```

gRPC request to Gateway Ingress 

Parameters 
---------- deployment_name  Deployment name of Seldon Deployment namespace  The namespace the Seldon Deployment is running in gateway_endpoint  The endpoint for gateway shape  The shape of the data data  The numpy array data to send headers  A Dict of key value pairs to add to gRPC HTTP Headers payload_type  payload - tensor, ndarray or tftensor bin_data  Binary data to send str_data  String data to send json_data  JSON data to send custom_data  Custom data to send grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes names  Column names call_credentials  Call credentials - see SeldonCallCredentials channel_credentials  Channel credentials - see SeldonChannelCredentials meta  Custom meta data map, supplied as tags client_return_type  the return type of all functions can be either dict or proto raw_data  Raw payload (dictionary or proto) given by the user 

Returns 
-------  A SeldonMessage proto response 


---

<a href="../seldon_core/seldon_client/rest_feedback_seldon#L1929"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rest_feedback_seldon`

```python
rest_feedback_seldon(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    prediction_truth: SeldonMessage = None,
    reward: float = 0,
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8002',
    client_return_type: str = 'proto',
    raw_request: dict = None,
    **kwargs
) → SeldonClientFeedback
```

Send Feedback to Seldon API Gateway using REST 

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback namespace  k8s namespace of running deployment client_return_type  the return type of all functions can be either dict or proto kwargs 

Returns 
------- 


---

<a href="../seldon_core/seldon_client/grpc_feedback_seldon#L2001"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grpc_feedback_seldon`

```python
grpc_feedback_seldon(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    prediction_truth: SeldonMessage = None,
    reward: float = 0,
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8004',
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    client_return_type: str = 'proto',
    raw_request: dict = None,
    **kwargs
) → SeldonClientFeedback
```

Send feedback to Seldon API gateway via gRPC 

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback namespace  k8s namespace of running deployment grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes client_return_type  the return type of all functions can be either dict or proto kwargs 

Returns 
------- 


---

<a href="../seldon_core/seldon_client/rest_feedback_gateway#L2074"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rest_feedback_gateway`

```python
rest_feedback_gateway(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    prediction_truth: SeldonMessage = None,
    reward: float = 0,
    deployment_name: str = '',
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8003',
    headers: Dict = None,
    gateway_prefix: str = None,
    client_return_type: str = 'proto',
    raw_request: dict = None,
    **kwargs
) → SeldonClientFeedback
```

Send Feedback to Seldon via gateway using REST 

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback deployment_name  The name of the running Seldon deployment namespace  k8s namespace of running deployment gateway_endpoint  The gateway host:port endpoint headers  Headers to add to the request gateway_prefix  The prefix to add to the request path for gateway client_return_type  the return type of all functions can be either dict or proto kwargs 

Returns 
-------  A Seldon Feedback Response 


---

<a href="../seldon_core/seldon_client/grpc_feedback_gateway#L2183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grpc_feedback_gateway`

```python
grpc_feedback_gateway(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    prediction_truth: SeldonMessage = None,
    reward: float = 0,
    deployment_name: str = '',
    namespace: str = None,
    gateway_endpoint: str = 'localhost:8003',
    headers: Dict = None,
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    client_return_type: str = 'proto',
    raw_request: dict = None,
    **kwargs
) → SeldonClientFeedback
```

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback deployment_name  The name of the running Seldon deployment namespace  k8s namespace of running deployment gateway_endpoint  The gateway host:port endpoint headers  Headers to add to the request grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes client_return_type  the return type of all functions can be either dict or proto kwargs 

Returns 
------- 


---

<a href="../seldon_core/seldon_client/SeldonClientException#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonClientException`
Seldon Client Exception 

<a href="../seldon_core/seldon_client/__init__#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message)
```









---

<a href="../seldon_core/seldon_client/SeldonChannelCredentials#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonChannelCredentials`
Channel credentials. 

Presently just denotes an SSL connection. For GRPC in order to be properly implemented, you need to provide *either* the root_certificate_files, *or* all the file paths. The verify attribute currently is used to avoid SSL verification in REST however for GRPC it is recommended that you provide a path at least for the root_certificates_file otherwise it may not work as expected. 

<a href="../seldon_core/seldon_client/__init__#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    verify: bool = True,
    root_certificates_file: str = None,
    private_key_file: str = None,
    certificate_chain_file: str = None
)
```









---

<a href="../seldon_core/seldon_client/SeldonCallCredentials#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonCallCredentials`
Credentials for each call, currently implements the ability to provide  an OAuth token which is currently made available through REST via  the X-Auth-Token header, and via GRPC via the metadata call creds. 

<a href="../seldon_core/seldon_client/__init__#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(token: str = None)
```









---

<a href="../seldon_core/seldon_client/SeldonClientPrediction#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonClientPrediction`
Data class to return from Seldon Client 

<a href="../seldon_core/seldon_client/__init__#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    request: Optional[SeldonMessage, Dict],
    response: Optional[SeldonMessage, Dict],
    success: bool = True,
    msg: str = ''
)
```









---

<a href="../seldon_core/seldon_client/SeldonClientFeedback#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonClientFeedback`
Data class to return from Seldon Client for feedback calls 

<a href="../seldon_core/seldon_client/__init__#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    request: Optional[Feedback],
    response: Optional[SeldonMessage, Dict],
    success: bool = True,
    msg: str = ''
)
```









---

<a href="../seldon_core/seldon_client/SeldonClientCombine#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonClientCombine`
Data class to return from Seldon Client for aggregate calls 

<a href="../seldon_core/seldon_client/__init__#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    request: Optional[SeldonMessageList],
    response: Optional[SeldonMessage],
    success: bool = True,
    msg: str = ''
)
```









---

<a href="../seldon_core/seldon_client/SeldonClient#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonClient`
A reference Seldon API Client 

<a href="../seldon_core/seldon_client/__init__#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    gateway: str = 'ambassador',
    transport: str = 'rest',
    namespace: str = None,
    deployment_name: str = None,
    payload_type: str = 'tensor',
    gateway_endpoint: str = 'localhost:8003',
    microservice_endpoint: str = 'localhost:5000',
    grpc_max_send_message_length: int = 4194304,
    grpc_max_receive_message_length: int = 4194304,
    channel_credentials: SeldonChannelCredentials = None,
    call_credentials: SeldonCallCredentials = None,
    debug: bool = False,
    client_return_type: str = 'dict',
    ssl: bool = None
)
```

Parameters 
---------- gateway  API Gateway - either ambassador, istio or seldon transport  API transport - grpc or rest namespace  k8s namespace of running deployment deployment_name  name of seldon deployment payload_type  type of payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes client_return_type  the return type of all functions can be either dict or proto 




---

<a href="../seldon_core/seldon_client/explain#L498"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `explain`

```python
explain(
    gateway: str = None,
    transport: str = None,
    deployment_name: str = None,
    payload_type: str = None,
    gateway_endpoint: str = None,
    shape: Tuple = (1, 1),
    namespace: str = None,
    data: ndarray = None,
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: str = None,
    names: Iterable[str] = None,
    gateway_prefix: str = None,
    headers: Dict = None,
    http_path: str = None,
    client_return_type: str = None,
    predictor: str = None,
    ssl: bool = None
) → Dict
```

Parameters 
---------- gateway  API Gateway - either ambassador, istio or seldon transport  API transport - grpc or rest namespace  k8s namespace of running deployment deployment_name  name of seldon deployment payload_type  type of payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes data  Numpy Array Payload to send bin_data  Binary payload to send - will override data str_data  String payload to send - will override data json_data  JSON payload to send - will override data names  Column names gateway_prefix  prefix path for gateway URL endpoint headers  Headers to add to request http_path:  Custom http path for predict call to use client_return_type  the return type of all functions can be either dict or proto predictor  The name of the predictor to send the explanations to 

Returns 
------- 

---

<a href="../seldon_core/seldon_client/feedback#L382"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `feedback`

```python
feedback(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    prediction_truth: SeldonMessage = None,
    reward: float = 0,
    gateway: str = None,
    transport: str = None,
    deployment_name: str = None,
    payload_type: str = None,
    gateway_endpoint: str = None,
    microservice_endpoint: str = None,
    method: str = None,
    shape: Tuple = (1, 1),
    namespace: str = None,
    gateway_prefix: str = None,
    client_return_type: str = None,
    raw_request: dict = None,
    ssl: bool = None
) → SeldonClientFeedback
```

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback gateway  API Gateway - either ambassador, istio or seldon transport  API transport - grpc or rest deployment_name  name of seldon deployment payload_type  payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes method  The microservice method to call shape  The shape of the data to send namespace  k8s namespace of running deployment client_return_type  the return type of all functions can be either dict or proto 

Returns 
------- 

---

<a href="../seldon_core/seldon_client/microservice#L597"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `microservice`

```python
microservice(
    gateway: str = None,
    transport: str = None,
    deployment_name: str = None,
    payload_type: str = None,
    gateway_endpoint: str = None,
    microservice_endpoint: str = None,
    method: str = None,
    shape: Tuple = (1, 1),
    namespace: str = None,
    data: ndarray = None,
    datas: List[ndarray] = None,
    ndatas: int = None,
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    custom_data: Any = None,
    names: Iterable[str] = None
) → Union[SeldonClientPrediction, SeldonClientCombine]
```

Parameters 
---------- gateway  API Gateway - either ambassador, istio or seldon transport  API transport - grpc or rest deployment_name  name of seldon deployment payload_type  payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes method  The microservice method to call shape  The shape of the data to send namespace  k8s namespace of running deployment data  Numpy Array Payload to send bin_data  Binary payload to send - will override data str_data  String payload to send - will override data json_data  String payload to send - will override data custom_data  Custom payload to send - will override data ndatas  Multiple numpy arrays to send for aggregation bin_data  Binary data payload str_data  String data payload names  Column names 

Returns 
-------  A prediction result 

---

<a href="../seldon_core/seldon_client/microservice_feedback#L714"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `microservice_feedback`

```python
microservice_feedback(
    prediction_request: SeldonMessage = None,
    prediction_response: SeldonMessage = None,
    reward: float = 0,
    gateway: str = None,
    transport: str = None,
    deployment_name: str = None,
    payload_type: str = None,
    gateway_endpoint: str = None,
    microservice_endpoint: str = None,
    method: str = None,
    shape: Tuple = (1, 1),
    namespace: str = None
) → SeldonClientFeedback
```

Parameters 
---------- prediction_request  Previous prediction request prediction_response  Previous prediction response reward  A reward to send in feedback gateway  API Gateway - either Gateway or seldon transport  API transport - grpc or rest deployment_name  name of seldon deployment payload_type  payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes method  The microservice method to call shape  The shape of the data to send namespace  k8s namespace of running deployment 

Returns 
-------  A client response 

---

<a href="../seldon_core/seldon_client/predict#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `predict`

```python
predict(
    gateway: str = None,
    transport: str = None,
    deployment_name: str = None,
    payload_type: str = None,
    gateway_endpoint: str = None,
    microservice_endpoint: str = None,
    method: str = None,
    shape: Tuple = (1, 1),
    namespace: str = None,
    data: ndarray = None,
    bin_data: Union[bytes, bytearray] = None,
    str_data: str = None,
    json_data: Union[str, List, Dict] = None,
    custom_data: Any = None,
    names: Iterable[str] = None,
    gateway_prefix: str = None,
    headers: Dict = None,
    http_path: str = None,
    meta: Dict = None,
    client_return_type: str = None,
    raw_data: Dict = None,
    ssl: bool = None
) → SeldonClientPrediction
```

Parameters 
---------- gateway  API Gateway - either ambassador, istio or seldon transport  API transport - grpc or rest namespace  k8s namespace of running deployment deployment_name  name of seldon deployment payload_type  type of payload - tensor, ndarray or tftensor gateway_endpoint  Gateway endpoint microservice_endpoint  Running microservice endpoint grpc_max_send_message_length  Max grpc send message size in bytes grpc_max_receive_message_length  Max grpc receive message size in bytes data  Numpy Array Payload to send bin_data  Binary payload to send - will override data str_data  String payload to send - will override data json_data  JSON payload to send - will override data custom_data  Custom payload to send - will override data names  Column names gateway_prefix  prefix path for gateway URL endpoint headers  Headers to add to request http_path:  Custom http path for predict call to use meta:  Custom meta map, supplied as tags client_return_type  the return type of all functions can be either dict or proto raw_data  Raw payload, a dictionary representing the json request or the raw grpc proto 

Returns 
------- 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
