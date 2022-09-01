<!-- markdownlint-disable -->

<a href="../klops/seldon_core/auth/default.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.auth.default`
Default Module for Authentication Implementation 



---

<a href="../klops/seldon_core/auth/default.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DefaultAuthentication`
Default Class Implementation for Kubernetes authentication. 

<a href="../klops/seldon_core/auth/default.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    cluster_host: str = 'localhost',
    token: str = 'TokenString123',
    **kwargs: Any
) → None
```

_summary_ Default Class Implementation for Kubernetes authentication. 

**Args:**
 
 - <b>`cluster_host`</b> (str, optional):  _description_. Defaults to "localhost". 
 - <b>`token`</b> (str, optional):  _description_. Defaults to "TokenString123". 




---

<a href="../klops/seldon_core/auth/default.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_custer_endpoint`

```python
get_custer_endpoint() → str
```

_summary_ Get Default Cluster Host URI endpoint. 



**Returns:**
 
 - <b>`str`</b>:  _description_ A string of Basic Cluster Host URI endpoint. 

---

<a href="../klops/seldon_core/auth/default.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_token`

```python
get_token() → str
```

_summary_ Get Default Bearer Token String. 

**Returns:**
 
 - <b>`str`</b>:  _description_ A string of Bearer Token. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
