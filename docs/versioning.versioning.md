<!-- markdownlint-disable -->

<a href="../klops/versioning/versioning.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `versioning.versioning`
_summary_ Main module for versioning Control. 



---

<a href="../klops/versioning/versioning.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Versioning`
_summary_ Versioning control for klops. Based on DVC. 




---

<a href="../klops/versioning/versioning.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add`

```python
add(file_or_path: str) → None
```

_summary_ Track the file / path into DVC. 

**Args:**
 
 - <b>`file_or_path`</b> (str):  _description_ File or path tobe added. 

---

<a href="../klops/versioning/versioning.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_remote`

```python
add_remote(name: str, remote_url: str) → None
```

_summary_ Add remote repository. Could be local, or remote storage such as GCP bucket or AWS s3. 

**Args:**
 
 - <b>`remote_url`</b> (str):  _description_ 

---

<a href="../klops/versioning/versioning.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pull`

```python
pull() → None
```

_summary_ Pull the commited data. 

---

<a href="../klops/versioning/versioning.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `push`

```python
push() → None
```

_summary_ Push every tracked changes into dvc. 

---

<a href="../klops/versioning/versioning.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_binary`

```python
read_binary(file_name: str) → Any
```

_summary_ Read the binary file such as .pkl, .joblib, etc. stored in the DVC storage / repository. 

**Args:**
 
 - <b>`file_name`</b> (str):  _description_ The file name. Including its path. 



**Returns:**
 
 - <b>`Any`</b>:  _description_ Object pointer instances. 

---

<a href="../klops/versioning/versioning.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_dataset`

```python
read_dataset(file_name: str) → Any
```

_summary_ Read dataset from DVC artifact storage. 

**Args:**
 
 - <b>`file_name`</b> (str):  _description_ The file name. Including it's path. 



**Returns:**
 
 - <b>`Any`</b>:  _description_ The dataset buffer. Need to parse. 

---

<a href="../klops/versioning/versioning.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `repro`

```python
repro() → None
```

_summary_ Reproduce the DVC pipeline. 

---

<a href="../klops/versioning/versioning.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    entry_point: str,
    name: str = None,
    dependencies: List = [],
    outputs: List = []
) → None
```

_summary_ Run the defined DVC pipeline. 

**Args:**
 
 - <b>`entry_point`</b> (str):  _description_ The main program to be executed. 
 - <b>`name`</b> (str, optional):  _description_. Defaults to None. The Pipeline name. 
 - <b>`dependencies`</b> (List, optional):  _description_. Defaults to []. List of dependencies. The same as `-d` options in dvc command. 
 - <b>`outputs`</b> (List, optional):  _description_. Defaults to []. List of the outputs, The same as `-o` options in dvc command. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
