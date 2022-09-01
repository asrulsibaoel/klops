<!-- markdownlint-disable -->

<a href="../seldon_core/metadata#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.metadata`




**Global Variables**
---------------
- **MODEL_IMAGE**
- **SELDON_ARRAY_SCHEMA**
- **SELDON_JSON_SCHEMA**
- **SELDON_STR_SCHEMA**
- **SELDON_BIN_SCHEMA**
- **SELDON_CUSTOM_DEFINITION**
- **TENSOR_DATA_TYPES**
- **METADATA_TENSOR_SCHEMA**
- **INPUTS_OUTPUTS_SCHEMA**
- **JSON_SCHEMA**

---

<a href="../seldon_core/metadata/validate_model_metadata#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `validate_model_metadata`

```python
validate_model_metadata(data: Dict) → Dict
```

Validate metadata. 

Parameters 
---------- data  User defined model metadata (json) 

Returns 
-------  Validated model metadata (json) 

Raises 
------ SeldonInvalidMetadataError: if data cannot be properly validated 

Notes 
----- 

Read data from json and validate against v1 or v2 metadata schema. SeldonInvalidMetadataError exception will be raised if validation fails. 


---

<a href="../seldon_core/metadata/SeldonInvalidMetadataError#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonInvalidMetadataError`










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
