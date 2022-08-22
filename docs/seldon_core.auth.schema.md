<!-- markdownlint-disable -->

<a href="../klops/seldon_core/auth/schema.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.auth.schema`
Kubernetes authentication Basic Schema module. 



---

<a href="../klops/seldon_core/auth/schema.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AbstractKubernetesAuth`
Abstract Class for Kubernetes get authentication 

<a href="../klops/seldon_core/auth/schema.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(**kwargs) → None
```








---

<a href="../klops/seldon_core/auth/schema.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_custer_endpoint`

```python
get_custer_endpoint() → str
```

Get cluster host URI endpoint from platfroms. 

**Returns:**
  A string of host URI endpoint. 

---

<a href="../klops/seldon_core/auth/schema.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_token`

```python
get_token() → str
```

Get token string from platforms. 

**Returns:**
  A string of Authorization token. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
