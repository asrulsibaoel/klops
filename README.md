# Klops: Koinworks MLOps

[![Koinworks](https://codecov.io/gh/asrulsibaoel/python-packages-template/branch/main/graph/badge.svg?token=python-packages-template_token_here)](https://codecov.io/gh/asrulsibaoel/python-packages-template)
[![CI](https://github.com/asrulsibaoel/python-packages-template/actions/workflows/main.yml/badge.svg)](https://github.com/asrulsibaoel/python-packages-template/actions/workflows/main.yml)

Klops is an End-to-End machine learning development pipeline ops. Its build on top of Seldon Core, MLflow and DVC. The goal of this project is to make easier for Data Scientist to develop, maintain and deploy their machine learning projects.

## Installation  
### From PyPI
Using pip is the best option if you want to get the stable version and easier way to install.
```bash
pip install klops
```
### Build From Source  
This is the best way to get the lastest published library, including the experimental version.

Clone this repo  
```bash
git clone https://gitlab-engineering.koinworks.com/data-team/klops.git
```  
Change your directory to your klops folder:  
```bash
cd klops
```  
Run below command  
```bash
python setup.py install
```

## Features & Usages  
Klops consists of three modules. Versioning, Experiment and Deployment.

### Klops Deployment  
Klops Deployment is a module to deploy the development machine learning projects into Seldon Core instance. 

```py
from klops import BaseClass
from klops import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m klops
#or
$ klops
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
