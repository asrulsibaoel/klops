
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
    <a href="#" title="Project License"><img src="https://img.shields.io/badge/License-Koinworks-red"></a>
    <!-- <a href="https://gitter.im/ml-tooling/lazydocs" title="Chat on Gitter"><img src="https://badges.gitter.im/ml-tooling/lazydocs.svg"></a> -->
    <a href="https://twitter.com/mltooling" title="ML Tooling on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?label=follow&style=social"></a>
</p>

<p align="center">
  <a href="#installation">Getting Started</a> •
  <a href="/docs#tutorials-and-api-overview">Documentation</a> •
  <a href="/../../issues">Support</a> •
  <a href="#development">Contribution</a>
  <!-- <a href="https://github.com/ml-tooling/lazydocs/releases">Changelog</a> -->
</p>

Klops is an End-to-End machine learning development pipeline ops. Its build on top of Seldon Core, MLflow and DVC. The goal of this project is to make easier for Data Scientist to develop, maintain, log their experiments and deploy their machine learning projects.  

## Prerequisites  
- Seldon Core Installed on your Kubernetes cluster. Guidance [here](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/install.html)  
- MLflow Tracking Server deployed. Recommended to use the schenario 5  [here](https://www.mlflow.org/docs/latest/tracking.html#scenario-5-mlflow-tracking-server-enabled-with-proxied-artifact-storage-access)  
- Local or remote storage such as Amazon S3 or Google Cloud Storage (GCS) or similar.

## Installation  
### From PyPI
Using pip is the best option if you want to get the stable version and easier way to install.
```bash
$ pip install klops
```
### Build From Source  
This is the best way to get the lastest published library, including the experimental version.

Clone this repo  
```bash
$ git clone https://gitlab-engineering.koinworks.com/data-team/klops.git
```  
Change your directory to your klops folder:  
```bash
$ cd klops
```  
Install
```bash
$ python setup.py install
```

## Basic Usages 
Klops consists of three modules. Versioning, Experiment and Deployment.

### Klops Experiment  
Klops Experiment is a class that wraps the [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html). Below are the simple example to begin with.
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

You would see your experiment result in your Mlflow Tracking UI like below:  
![Tracking result](/resources/images/experiment_ui.png)
For the complete tutorials could be seen through this [documentation](/docs/tutorial.experiment.md).  
### Klops Versioning  
Klops Versioning is a kind of version control based on DVC. This module wrapped the commandline and python APIs from [DVC](https://dvc.org).
```py
from klops.versioning import Versioning

versioning = Versioning()

# Track your file into dvc
versioning.add("myfile.csv")

# Add your DVC repository storage
versioning.add_remote("gs://your-bucket-name/your-path/")

# Push your changes to DVC
versioning.push()
```  

Complete examples could be seen on this [tutorial](/docs/tutorial.versioning.md) page.  

### Klops Deployment  
Klops Deployment is a module to deploy the development machine learning projects into Seldon Core instance. Below is the example on how to done with.

```py
from klops.seldon_core import SeldonDeployment
from klops.seldon_core.auth import GKEAuthentication

gke = GKEAuthentication(
    project_id="your-project-id",
    zone="your-project-region",
    cluster_id="your-cluster-id")
deployment = SeldonDeployment(gke, "seldon")

## Config file could be json or yaml/yml file.
config = deployment.load_deployment_configuration("<deployment-config>.json")
deployment.deploy(config)
```  
Now you can access your API through this doc `http://<ingress_url>/seldon/<namespace>/<model-name>/api/v1.0/doc/`. Example result:  
![Deployment Example](/resources/images/deployment_result_example.jpg)

## Development  

We are open for anyone who wants to contribute! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
