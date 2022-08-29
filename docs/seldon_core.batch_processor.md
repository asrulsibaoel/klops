<!-- markdownlint-disable -->

<a href="../seldon_core/batch_processor#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `seldon_core.batch_processor`




**Global Variables**
---------------
- **SELDON_PUID_HEADER**
- **CHOICES_GATEWAY_TYPE**
- **CHOICES_TRANSPORT**
- **CHOICES_PAYLOAD_TYPE**
- **CHOICES_DATA_TYPE**
- **CHOICES_METHOD**
- **CHOICES_LOG_LEVEL**

---

<a href="../seldon_core/batch_processor/setup_logging#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `setup_logging`

```python
setup_logging(log_level: str)
```






---

<a href="../seldon_core/batch_processor/start_multithreaded_batch_worker#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `start_multithreaded_batch_worker`

```python
start_multithreaded_batch_worker(
    deployment_name: str,
    gateway_type: str,
    namespace: str,
    host: str,
    transport: str,
    data_type: str,
    payload_type: str,
    workers: int,
    retries: int,
    batch_size: int,
    input_data_path: str,
    output_data_path: str,
    method: str,
    log_level: str,
    benchmark: bool,
    batch_id: str,
    batch_interval: float,
    call_credentials_token: str,
    use_ssl: bool,
    ssl_verify: bool
) → None
```

Starts the multithreaded batch worker which consists of three worker types and two queues; the input_file_worker which reads a file and puts all lines in an input queue, which are then read by the multiple request_processor_workers (the number of parallel workers is specified by the workers param), which puts the output in the output queue and then the output_file_worker which puts all the outputs in the output file in a thread-safe approach. 

All parameters are defined and explained in detail in the run_cli function. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
