<!-- markdownlint-disable -->

<a href="../seldon_core/flask_utils#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.flask_utils`




**Global Variables**
---------------
- **ANNOTATIONS_FILE**
- **ANNOTATION_GRPC_MAX_MSG_SIZE**
- **DEFAULT_ANNOTATION_REST_TIMEOUT**
- **ANNOTATION_REST_TIMEOUT**

---

<a href="../seldon_core/flask_utils/get_multi_form_data_request#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_multi_form_data_request`

```python
get_multi_form_data_request() → Dict
```

Parses a request submitted with Content-type:multipart/form-data all the keys under SeldonMessage are accepted as form input binData can only be passed as file input strData can be passed as file or text input the file input is base64 encoded 

Returns 
-------  JSON Dict 


---

<a href="../seldon_core/flask_utils/get_request#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_request`

```python
get_request(skip_decoding=False) → Union[Dict, bytes]
```

Parse a request to get JSON dict 

Returns 
-------  JSON Dict 


---

<a href="../seldon_core/flask_utils/jsonify#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `jsonify`

```python
jsonify(response, skip_encoding=False)
```






---

<a href="../seldon_core/flask_utils/SeldonMicroserviceException#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonMicroserviceException`




<a href="../seldon_core/flask_utils/__init__#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    message,
    status_code=None,
    payload=None,
    reason='MICROSERVICE_BAD_DATA'
)
```








---

<a href="../seldon_core/flask_utils/to_dict#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
