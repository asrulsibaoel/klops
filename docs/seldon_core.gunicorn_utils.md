<!-- markdownlint-disable -->

<a href="../seldon_core/gunicorn_utils#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.gunicorn_utils`





---

<a href="../seldon_core/gunicorn_utils/post_worker_init#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `post_worker_init`

```python
post_worker_init(worker)
```






---

<a href="../seldon_core/gunicorn_utils/worker_exit#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `worker_exit`

```python
worker_exit(server, worker, seldon_metrics: SeldonMetrics)
```






---

<a href="../seldon_core/gunicorn_utils/accesslog#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `accesslog`

```python
accesslog(flag: bool) → Optional[str]
```

Enable / disable access log in Gunicorn depending on the flag. 


---

<a href="../seldon_core/gunicorn_utils/threads#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `threads`

```python
threads(threads: int, single_threaded: bool) → int
```

Number of threads to run in each Gunicorn worker. 


---

<a href="../seldon_core/gunicorn_utils/StandaloneApplication#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `StandaloneApplication`
Standalone Application to run a Flask app in Gunicorn. 

<a href="../seldon_core/gunicorn_utils/__init__#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(app, options: Dict = None)
```








---

<a href="../seldon_core/gunicorn_utils/load#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load`

```python
load()
```





---

<a href="../seldon_core/gunicorn_utils/load_config#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load_config`

```python
load_config()
```






---

<a href="../seldon_core/gunicorn_utils/UserModelApplication#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UserModelApplication`
Gunicorn application to run a Flask app in Gunicorn loading first the user's model. 

<a href="../seldon_core/gunicorn_utils/__init__#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    app,
    user_object,
    tracing,
    jaeger_extra_tags,
    interface_name,
    options: Dict = None
)
```








---

<a href="../seldon_core/gunicorn_utils/load#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load`

```python
load()
```





---

<a href="../seldon_core/gunicorn_utils/load_config#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load_config`

```python
load_config()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
