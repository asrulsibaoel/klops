<!-- markdownlint-disable -->

<a href="../seldon_core/serving_test_gen#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.serving_test_gen`
Contains methods to generate a JSON file for Seldon API integration testing. 

**Global Variables**
---------------
- **RANGE_INTEGER_MIN**
- **RANGE_INTEGER_MAX**
- **RANGE_FLOAT_MIN**
- **RANGE_FLOAT_MAX**

---

<a href="../seldon_core/serving_test_gen/create_seldon_api_testing_file#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_seldon_api_testing_file`

```python
create_seldon_api_testing_file(
    data: DataFrame,
    target: str,
    output_path: str
) → bool
```

Create a JSON file for Seldon API testing. 

Parameters 
---------- data  Pandas DataFrame used as a recipe for the json file. target  Name of the target column. output_path  Path of output file. 

Returns 
-------  True if file correctly generated. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
