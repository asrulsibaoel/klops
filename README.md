
<h1 align="center">
    Klops: Koin MLOps
</h1>

<p align="center">
    <strong>Build your end-to-end machine learning projects within one tool.</strong>
</p>

<p align="center">
    <a href="#" title="PyPi Version"><img src="https://img.shields.io/badge/PyPi-v.0.4.8-blue"></a>
    <a href="#" title="Python Version"><img src="https://img.shields.io/badge/Python-3.6%2B-green"></a>
    <!-- <a href="https://www.codacy.com/gh/ml-tooling/lazydocs/dashboard" title="Codacy Analysis"><img src="https://app.codacy.com/project/badge/Grade/1c8ad486ce9547b6b713cce7ca1d1ec3"></a> -->
    <!-- <a href="" title="Build status"><img src="https://img.shields.io/github/workflow/status/ml-tooling/lazydocs/build-pipeline?style=flat"></a> -->
    <a href="#" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat"></a>
    <!-- <a href="https://gitter.im/ml-tooling/lazydocs" title="Chat on Gitter"><img src="https://badges.gitter.im/ml-tooling/lazydocs.svg"></a> -->
    <a href="https://twitter.com/mltooling" title="ML Tooling on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?label=follow&style=social"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="/documentation">Documentation</a> •
  <a href="#support--feedback">Support</a> •
  <a href="#contribution">Contribution</a>
  <!-- <a href="https://github.com/ml-tooling/lazydocs/releases">Changelog</a> -->
</p>

Klops is an End-to-End machine learning development pipeline ops. Its build on top of Seldon Core, MLflow and DVC. The goal of this project is to make easier for Data Scientist to develop, maintain, log their experiments and deploy their machine learning projects.

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

## Usages 
Klops consists of three modules. Versioning, Experiment and Deployment.

### Klops Experiment  
#### Experiment without Tuner  
Below is the example how to start Experiment without using tuner.
```py
from klops.experiment import Experiment
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

experiment = Experiment(name="your-experiment-name", tracking_uri="http://<your-mlflow-host>:<port>")

X, y = load_iris(return_X_y=True)
HYPERPARAMETERS = {
    "n_estimators": 20,
    "max_depth": 10,
    "min_samples_split": 5
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner_args=HYPERPARAMETERS)
```
#### Experiment with HyperOpt Tuner  
Below is the example how to start Experiment without using tuner.
```py
from klops.experiment import Experiment
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

from hyperopt import hp
from hyperopt.pyll import scope

experiment = Experiment(name="your-experiment-name", tracking_uri="http://<your-mlflow-host>:<port>")

X, y = load_iris(return_X_y=True)
SEARCH_SPACE = {
    "n_estimators": scope.int(hp.quniform("n_estimators", 10, 50, 1)),
    "max_depth": scope.int(hp.quniform("max_depth", 10, 30, 1))
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner=None, tuner_args=SEARCH_SPACE)
```
#### Experiment with GridsearchCV Tuner  
Below is the example how to start Experiment without using tuner.
```py
from klops.experiment import Experiment
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

experiment = Experiment(name="your-experiment-name", tracking_uri="http://<your-mlflow-host>:<port>")

X, y = load_iris(return_X_y=True)
GRID_PARAMS = {
    "n_estimators": [10, 20, 50],
    "max_depth": [10, 20, 30]
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner='gridsearch', tuner_args=GRID_PARAMS)
```
### Klops Versioning  
Klops Versioning is kind of version control based on DVC. This module 

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
