<!-- markdownlint-disable -->

<a href="../klops/versioning/versioning.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `versioning.versioning`
Main module for versioning Control. 



---

<a href="../klops/versioning/versioning.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Versioning`
Versioning control for klops. Based on DVC. 




---

<a href="../klops/versioning/versioning.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add`

```python
add(file_or_path: str) → None
```

Track the file / path into DVC. 

**Args:**
 
 - <b>`file_or_path`</b> (str):   File or path tobe added. 

---

<a href="../klops/versioning/versioning.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_remote`

```python
add_remote(name: str, remote_url: str) → None
```

Add remote repository. Could be local, or remote storage such as GCP bucket or AWS s3. 

**Args:**
 
 - <b>`remote_url`</b> (str):  The remove URL for the DVC remote repository. 

---

<a href="../klops/versioning/versioning.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_url`

```python
get_url(path: str, repo: str = None, rev: str = None, remote: str = None) → Any
```

Get the URL to the storage location of a data file or             directory tracked in a DVC project. 



**Args:**
 
 - <b>`path`</b> (str):  Path to the data file or directory. 
 - <b>`repo`</b> (str, optional):  Repository URL. Defaults to None. 
 - <b>`rev`</b> (str, optional):  Revision or tags that already defined in git. Defaults to None. 
 - <b>`remote`</b> (str, optional):  Remote URL for the repository. Defaults to None. 



**Returns:**
 
 - <b>`Any`</b>:  Returns the URL string of the storage location (in a DVC remote)                 where a target file or directory, specified by its path in a repo                     (DVC project), is stored. 

---

<a href="../klops/versioning/versioning.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init`

```python
init() → None
```

Initiate DVC 

Initiate the DVC when it's not found. 

---

<a href="../klops/versioning/versioning.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `params_show`

```python
params_show(
    *targets: str,
    stages: Optional[str, Iterable[str]] = None,
    repo: Optional[str] = None,
    rev: Optional[str] = None,
    deps: bool = False
) → Dict
```

Get parameters tracked in `repo`. 

Without arguments, this function will retrieve all params from all tracked parameter files, for the current working tree. 

See the options below to restrict the parameters retrieved. 



**Args:**
 
 - <b>`*targets (str, optional)`</b>:  Names of the parameter files to retrieve params from. For example, "params.py, myparams.toml". If no `targets` are provided, all parameter files tracked in `dvc.yaml` will be used. Note that targets don't necessarily have to be defined in `dvc.yaml`. 
 - <b>`repo`</b> (str, optional):  location of the DVC repository.  Defaults to the current project (found by walking up from the  current working directory tree).  It can be a URL or a file system path.  Both HTTP and SSH protocols are supported for online Git repos 
 - <b>`(e.g. [user@]server`</b>: project.git). 
 - <b>`stages`</b> (Union[str, Iterable[str]], optional):  Name or names of the  stages to retrieve parameters from.  Defaults to `None`.  If `None`, all parameters from all stages will be retrieved.  If this method is called from a different location to the one where  the `dvc.yaml` is found, the relative path to the `dvc.yaml` must 
 - <b>`be provided as a prefix with the syntax `{relpath}`</b>: {stage}`. 
 - <b>`For example`</b>:  `subdir/dvc.yaml:stage-0` or `../dvc.yaml:stage-1`. 
 - <b>`rev`</b> (str, optional):  Name of the `Git revision`_ to retrieve parameters  from.  Defaults to `None`.  An example of git revision can be a branch or tag name, a commit  hash or a dvc experiment name.  If `repo` is not a Git repo, this option is ignored.  If `None`, the current working tree will be used. 
 - <b>`deps`</b> (bool, optional):  Whether to retrieve only parameters that are  stage dependencies or not.  Defaults to `False`. 



**Returns:**
 
 - <b>`Dict`</b>:  See Examples below. 



**Raises:**
 
 - <b>`DvcException`</b>:  If no params are found in `repo`. 



**Examples:**
 


    - No arguments. 

Working on https://github.com/iterative/example-get-started 

``` import json```
    >>> import dvc.api
    >>> params = dvc.api.params_show()
    >>> print(json.dumps(params, indent=4))
    {
         "prepare": {
             "split": 0.2,
             "seed": 20170428
         },
         "featurize": {
             "max_features": 200,
             "ngrams": 2
         },
         "train": {
             "seed": 20170428,
             "n_est": 50,
             "min_split": 0.01
         }
    }


        ---


        - Filtering with `stages`.

    Working on https://github.com/iterative/example-get-started

    `stages` can a single string:

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show(stages="prepare")
    >>> print(json.dumps(params, indent=4))
    {
         "prepare": {
             "split": 0.2,
             "seed": 20170428
         }
    }

    Or an iterable of strings:

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show(stages=["prepare", "train"])
    >>> print(json.dumps(params, indent=4))
    {
         "prepare": {
             "split": 0.2,
             "seed": 20170428
         },
         "train": {
             "seed": 20170428,
             "n_est": 50,
             "min_split": 0.01
         }
    }


        ---


        - Using `rev`.

    Working on https://github.com/iterative/example-get-started

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show(rev="tune-hyperparams")
    >>> print(json.dumps(params, indent=4))
    {
         "prepare": {
             "split": 0.2,
             "seed": 20170428
         },
         "featurize": {
             "max_features": 200,
             "ngrams": 2
         },
         "train": {
             "seed": 20170428,
             "n_est": 100,
             "min_split": 8
         }
    }


        ---


        - Using `targets`.

    Working on `multi-params-files` folder of
    https://github.com/iterative/pipeline-conifguration

    You can pass a single target:

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show("params.yaml")
    >>> print(json.dumps(params, indent=4))
    {
         "run_mode": "prod",
         "configs": {
             "dev": "configs/params_dev.yaml",
             "test": "configs/params_test.yaml",
             "prod": "configs/params_prod.yaml"
         },
         "evaluate": {
             "dataset": "micro",
             "size": 5000,
             "metrics": ["f1", "roc-auc"],
             "metrics_file": "reports/metrics.json",
             "plots_cm": "reports/plot_confusion_matrix.png"
         }
    }


    Or multiple targets:

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show(
    ...     "configs/params_dev.yaml", "configs/params_prod.yaml")
    >>> print(json.dumps(params, indent=4))
    {
         "configs/params_prod.yaml:run_mode": "prod",
         "configs/params_prod.yaml:config_file": "configs/params_prod.yaml",
         "configs/params_prod.yaml:data_load": {
             "dataset": "large",
             "sampling": {
             "enable": true,
             "size": 50000
             }
         },
         "configs/params_prod.yaml:train": {
             "epochs": 1000
         },
         "configs/params_dev.yaml:run_mode": "dev",
         "configs/params_dev.yaml:config_file": "configs/params_dev.yaml",
         "configs/params_dev.yaml:data_load": {
             "dataset": "development",
             "sampling": {
             "enable": true,
             "size": 1000
             }
         },
         "configs/params_dev.yaml:train": {
             "epochs": 10
         }
    }


        ---


        - Git URL as `repo`.

    >>> import json
    >>> import dvc.api
    >>> params = dvc.api.params_show(
    ...     repo="https://github.com/iterative/demo-fashion-mnist")
    {
         "train": {
             "batch_size": 128,
             "hidden_units": 64,
             "dropout": 0.4,
             "num_epochs": 10,
             "lr": 0.001,
             "conv_activation": "relu"
         }
    }


.. _Git revision:
    https://git-scm.com/docs/revisions


---

<a href="../klops/versioning/versioning.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pull`

```python
pull() → None
```

Pull the commited data. 

---

<a href="../klops/versioning/versioning.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `push`

```python
push() → None
```

Push every tracked changes into dvc. 

---

<a href="../klops/versioning/versioning.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../klops/versioning/versioning.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_dataset`

```python
read_dataset(file_name: str, rev: str = None, remote: str = None) → Any
```

Read dataset from DVC artifact storage. 

**Args:**
 
 - <b>`file_name`</b> (str):  The file name. Including it's path. 
 - <b>`rev`</b> (str, optional):  Revision or tags that already defined in git. Defaults to None. 
 - <b>`remote`</b> (str, optional):  Remote repository URL. Defaults to None. 

**Returns:**
 
 - <b>`Any`</b>:   The dataset file buffer. Need to parse. 

---

<a href="../klops/versioning/versioning.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `repro`

```python
repro() → None
```

Reproduce the DVC pipeline. 

---

<a href="../klops/versioning/versioning.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 - <b>`name`</b> (str, optional):  Defaults to None. The Pipeline name. 
 - <b>`dependencies`</b> (List, optional):  Defaults to []. List of dependencies.                 The same as `-d` options in dvc command. 
 - <b>`outputs`</b> (List, optional):  Defaults to []. List of the outputs, The same as `-o`                 options in dvc command. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
