<!-- markdownlint-disable -->

<a href="../seldon_core/microservice_tester#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.microservice_tester`





---

<a href="../seldon_core/microservice_tester/gen_continuous#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gen_continuous`

```python
gen_continuous(
    f_range: Tuple[Union[float, str], Union[float, str]],
    n: int
) → ndarray
```

Create a continuous feature based on given range 

Parameters 
---------- f_range  A range tuple n  The number of feature values to create 

Returns 
------- 


---

<a href="../seldon_core/microservice_tester/reconciliate_cont_type#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `reconciliate_cont_type`

```python
reconciliate_cont_type(feature: ndarray, dtype: str) → ndarray
```

Ensure numpy arrays are always of type float 

Parameters 
---------- feature  Feature values dtype  The required type in the contract 

Returns 
-------  Numpy array 


---

<a href="../seldon_core/microservice_tester/gen_categorical#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gen_categorical`

```python
gen_categorical(values: List[str], n: List[int]) → ndarray
```

Generate a random categorical feature 

Parameters 
---------- values  The list of categorical values n  The number of features to create 

Returns 
-------  Numpy array of values 


---

<a href="../seldon_core/microservice_tester/generate_batch#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `generate_batch`

```python
generate_batch(contract: Dict, n: int, field: str) → ndarray
```






---

<a href="../seldon_core/microservice_tester/unfold_contract#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unfold_contract`

```python
unfold_contract(contract: Dict) → Dict
```

Expand contract to full version 

Parameters 
---------- contract  The Seldon Contract 

Returns 
-------  Full contract 


---

<a href="../seldon_core/microservice_tester/get_class_names#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_class_names`

```python
get_class_names(contract: Dict) → List[str]
```






---

<a href="../seldon_core/microservice_tester/run_send_feedback#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_send_feedback`

```python
run_send_feedback(args)
```

Make a feedback call to microservice 

Parameters 
---------- args  Command line args 


---

<a href="../seldon_core/microservice_tester/run_method#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_method`

```python
run_method(args, method)
```

Make a predict call to microservice 

Parameters 
---------- args  Command line args 


---

<a href="../seldon_core/microservice_tester/main#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

<a href="../seldon_core/microservice_tester/SeldonTesterException#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SeldonTesterException`




<a href="../seldon_core/microservice_tester/__init__#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(message)
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
