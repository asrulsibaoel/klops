<!-- markdownlint-disable -->

<a href="../klops/versioning/versioning.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `versioning.versioning`
Main module for versioning Control. 



---

<a href="../klops/versioning/versioning.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Versioning`
Versioning control for klops. Based on DVC. 




---

<a href="../klops/versioning/versioning.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add`

```python
add(file_or_path: str) → None
```

Track the file / path into DVC. 

**Args:**
 
 - <b>`file_or_path`</b> (str):   File or path tobe added. 

---

<a href="../klops/versioning/versioning.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_remote`

```python
add_remote(name: str, remote_url: str) → None
```

Add remote repository. Could be local, or remote storage such as GCP bucket or AWS s3. 

**Args:**
 
 - <b>`remote_url`</b> (str):  The remove URL for the DVC remote repository. 

---

<a href="../klops/versioning/versioning.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_url`

```python
get_url(path: str, repo: str = None, rev: str = None, remote: str = None) → Any
```

Get the URL to the storage location of a data file or             directory tracked in a DVC project. 



**Args:**
  path (str):  
 - <b>`repo`</b> (str, optional):  . Defaults to None. 
 - <b>`rev`</b> (str, optional):  . Defaults to None. 
 - <b>`remote`</b> (str, optional):  . Defaults to None. 



**Returns:**
 
 - <b>`Any`</b>:  Returns the URL string of the storage location (in a DVC remote)                 where a target file or directory, specified by its path in a repo                     (DVC project), is stored. 

---

<a href="../klops/versioning/versioning.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init`

```python
init() → None
```

Initiate DVC 

Initiate the DVC when it's not found. 

---

<a href="../klops/versioning/versioning.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pull`

```python
pull() → None
```

Pull the commited data. 

---

<a href="../klops/versioning/versioning.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `push`

```python
push() → None
```

Push every tracked changes into dvc. 

---

<a href="../klops/versioning/versioning.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_binary`

```python
read_binary(file_name: str) → Any
```

Read the binary file such as .pkl, .joblib, etc. stored in the DVC storage / repository. 

**Args:**
 
 - <b>`file_name`</b> (str):   The file name. Including its path. 



**Returns:**
 
 - <b>`Any`</b>:   Object pointer instances. 

---

<a href="../klops/versioning/versioning.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_dataset`

```python
read_dataset(file_name: str, revision: str = None) → Any
```

Read dataset from DVC artifact storage. 

**Args:**
 
 - <b>`file_name`</b> (str):   The file name. Including it's path. 



**Returns:**
 
 - <b>`Any`</b>:   The dataset buffer. Need to parse. 

---

<a href="../klops/versioning/versioning.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `repro`

```python
repro() → None
```

Reproduce the DVC pipeline. 

---

<a href="../klops/versioning/versioning.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    entry_point: str,
    name: str = None,
    dependencies: List = [],
    outputs: List = []
) → None
```

Run the defined DVC pipeline. 

**Args:**
 
 - <b>`entry_point`</b> (str):   The main program to be executed. 
 - <b>`name`</b> (str, optional):  . Defaults to None. The Pipeline name. 
 - <b>`dependencies`</b> (List, optional):  . Defaults to []. List of dependencies. The same as `-d` options in dvc command. 
 - <b>`outputs`</b> (List, optional):  . Defaults to []. List of the outputs, The same as `-o` options in dvc command. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
