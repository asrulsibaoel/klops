<!-- markdownlint-disable -->

<a href="../seldon_core/utils#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.utils`




**Global Variables**
---------------
- **ENV_MODEL_IMAGE**
- **ENV_MODEL_NAME**
- **NONIMPLEMENTED_IMAGE_MSG**
- **NONIMPLEMENTED_MSG**

---

<a href="../seldon_core/utils/get_request_path#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_request_path`

```python
get_request_path()
```






---

<a href="../seldon_core/utils/json_to_seldon_message#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `json_to_seldon_message`

```python
json_to_seldon_message(message_json: Union[List, Dict]) → SeldonMessage
```

Parses JSON input to a SeldonMessage proto 

Parameters 
---------- message_json  JSON input 

Returns 
-------  SeldonMessage 


---

<a href="../seldon_core/utils/json_to_seldon_model_metadata#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `json_to_seldon_model_metadata`

```python
json_to_seldon_model_metadata(metadata_json: Dict) → SeldonModelMetadata
```

Parses JSON input to SeldonModelMetadata proto 

Parameters 
---------- metadata_json  JSON input 

Returns 
-------  SeldonModelMetadata 


---

<a href="../seldon_core/utils/json_to_feedback#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `json_to_feedback`

```python
json_to_feedback(message_json: Dict) → Feedback
```

Parse a JSON message to a Feedback proto 

Parameters 
---------- message_json  Input json message Returns 
-------  A SeldonMessage 


---

<a href="../seldon_core/utils/json_to_seldon_messages#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `json_to_seldon_messages`

```python
json_to_seldon_messages(message_json: Dict) → SeldonMessageList
```






---

<a href="../seldon_core/utils/seldon_message_to_json#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `seldon_message_to_json`

```python
seldon_message_to_json(message_proto: SeldonMessage) → Dict
```

Convert a SeldonMessage proto to JSON Dict 

Parameters 
---------- message_proto  SeldonMessage proto Returns 
-------  JSON Dict 


---

<a href="../seldon_core/utils/seldon_messages_to_json#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `seldon_messages_to_json`

```python
seldon_messages_to_json(message_protos: SeldonMessageList) → Dict
```

Convert a SeldonMessage proto list to JSON Dict 

Parameters 
---------- message_protos  SeldonMessage protos Returns 
-------  JSON Dict 


---

<a href="../seldon_core/utils/feedback_to_json#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `feedback_to_json`

```python
feedback_to_json(message_proto: Feedback) → Dict
```

Convert a SeldonMessage proto to JSON Dict 

Parameters 
---------- message_proto  SeldonMessage proto 

Returns 
-------  JSON Dict 


---

<a href="../seldon_core/utils/get_data_from_proto#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_data_from_proto`

```python
get_data_from_proto(request: SeldonMessage) → Union[ndarray, str, bytes, dict]
```

Extract the data payload from the SeldonMessage 

Parameters 
---------- request  SeldonMessage 

Returns 
-------  Data payload as numpy array or the raw message format. Numpy array will be returned if the "data" field was used. 


---

<a href="../seldon_core/utils/grpc_datadef_to_array#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grpc_datadef_to_array`

```python
grpc_datadef_to_array(datadef: DefaultData) → ndarray
```

Convert a SeldonMessage DefaultData to a numpy array. 

Parameters 
---------- datadef  SeldonMessage DefaultData 

Returns 
-------  A numpy array 


---

<a href="../seldon_core/utils/get_meta_from_proto#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_meta_from_proto`

```python
get_meta_from_proto(request: SeldonMessage) → Dict
```

Convert SeldonMessage proto meta into Dict 

Parameters 
---------- request  SeldonMessage proto 

Returns 
-------  Dict 


---

<a href="../seldon_core/utils/array_to_rest_datadef#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `array_to_rest_datadef`

```python
array_to_rest_datadef(
    data_type: str,
    array: ndarray,
    names: Optional[List[str]] = []
) → Dict
```

Construct a payload Dict from a numpy array 

Parameters 
---------- data_type array names 

Returns 
-------  Dict representing Seldon payload 


---

<a href="../seldon_core/utils/array_to_grpc_datadef#L296"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `array_to_grpc_datadef`

```python
array_to_grpc_datadef(
    data_type: str,
    array: ndarray,
    names: Optional[Iterable[str]] = []
) → DefaultData
```

Convert numpy array and optional column names into a SeldonMessage DefaultData proto 

Parameters 
---------- array  numpy array names  column names data_type  The SeldonMessage type to convert to 

Returns 
-------  SeldonMessage DefaultData 


---

<a href="../seldon_core/utils/array_to_list_value#L339"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `array_to_list_value`

```python
array_to_list_value(array: ndarray, lv: Optional[ListValue] = None) → ListValue
```

Construct a proto ListValue from numpy array 

Parameters 
---------- array  Numpy array lv  Proto buffer ListValue to extend 

Returns 
------- ListValue protobuf 


---

<a href="../seldon_core/utils/construct_response_json#L366"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `construct_response_json`

```python
construct_response_json(
    user_model: SeldonComponent,
    is_request: bool,
    client_request_raw: Union[List, Dict],
    client_raw_response: Union[ndarray, str, bytes, dict],
    meta: dict = None,
    custom_metrics: List[Dict] = None,
    runtime_tags: Dict = None
) → Union[List, Dict]
```

This class converts a raw REST response into a JSON object that has the same structure as the SeldonMessage proto. This is necessary as the conversion using the SeldonMessage proto changes the Numeric types of all ints in a JSON into Floats. 

Parameters 
---------- user_model  Client user class is_request  Whether this is part of the request flow as opposed to the response flow client_request_raw  The request received in JSON format client_raw_response  The raw client response from their model 

Returns 
-------  A SeldonMessage JSON response 


---

<a href="../seldon_core/utils/construct_response#L492"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `construct_response`

```python
construct_response(
    user_model: SeldonComponent,
    is_request: bool,
    client_request: SeldonMessage,
    client_raw_response: Union[ndarray, str, bytes, dict, Any],
    meta: dict = None,
    custom_metrics: List[Dict] = None,
    runtime_tags: Dict = None
) → SeldonMessage
```

Parameters 
---------- user_model  Client user class is_request  Whether this is part of the request flow as opposed to the response flow client_request  The request received client_raw_response  The raw client response from their model 

Returns 
-------  A SeldonMessage proto response 


---

<a href="../seldon_core/utils/extract_request_parts_json#L591"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_request_parts_json`

```python
extract_request_parts_json(
    request: Union[Dict, List]
) → Tuple[Union[ndarray, str, bytes, Dict, List], Optional[Dict], Union[ndarray, str, bytes, Dict, List, NoneType], str]
```

Parameters 
---------- request  Input request in JSON format 

Returns 
-------  Key parts of the request extracted 


---

<a href="../seldon_core/utils/extract_request_parts#L645"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_request_parts`

```python
extract_request_parts(
    request: SeldonMessage
) → Tuple[Union[ndarray, str, bytes, dict], Dict, DefaultData, str]
```

Parameters 
---------- request  Input request 

Returns 
-------  Key parts of the request extracted 


---

<a href="../seldon_core/utils/extract_feedback_request_parts#L667"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_feedback_request_parts`

```python
extract_feedback_request_parts(
    request: Feedback
) → Tuple[DefaultData, ndarray, ndarray, float]
```

Extract key parts of the Feedback Message 

Parameters 
---------- request  Feedback proto 

Returns 
-------  Tuple of parts including extracted payloads 


---

<a href="../seldon_core/utils/getenv#L689"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `getenv`

```python
getenv(*env_vars, default=None)
```

Overload of os.getenv() to allow falling back through multiple environment variables. The environment variables will be checked sequentially until one of them is found. 

Parameters 
------ *env_vars  Variadic list of environment variable names to check. default  Default value to return if none of the environment variables exist. 

Returns 
------  Value of the first environment variable set or default. 


---

<a href="../seldon_core/utils/getenv_as_bool#L713"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `getenv_as_bool`

```python
getenv_as_bool(*env_vars, default=False)
```

Read environment variable, parsing it to a boolean. 


---

<a href="../seldon_core/utils/setup_tracing#L726"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `setup_tracing`

```python
setup_tracing(interface_name: str) → object
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
