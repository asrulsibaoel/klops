# Klops Experiment  
Klops Experiment is a class that wraps the [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html). Below are the complete tutorials to begin our experiment.

First, we need to instantiate the class API.  
```py
from klops.experiment import Experiment
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

experiment = Experiment(name="your-experiment-name", tracking_uri="http://<your-mlflow-host>:<port>")

X, y = load_iris(return_X_y=True)
```

## Experiment Options  
### Experiment without Tuner  
Below is the example how to start Experiment without using tuner.
```py
HYPERPARAMETERS = {
    "n_estimators": 20,
    "max_depth": 10,
    "min_samples_split": 5
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner_args=HYPERPARAMETERS)
```
### Experiment with HyperOpt Tuner  
Below is the example how to start Experiment using [hyperopt](http://hyperopt.github.io/hyperopt/) library as the tuner.
```py
from hyperopt import hp
from hyperopt.pyll import scope

SEARCH_SPACE = {
    "n_estimators": scope.int(hp.quniform("n_estimators", 10, 50, 1)),
    "max_depth": scope.int(hp.quniform("max_depth", 10, 30, 1))
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner=None, tuner_args=SEARCH_SPACE)
```
### Experiment with GridsearchCV Tuner  
We also provides GridsearchCV as our tunner. Below is the example how to done with.
```py
GRID_PARAMS = {
    "n_estimators": [10, 20, 50],
    "max_depth": [10, 20, 30]
}

experiment.start(GaussianNB, x_train_data=X, y_train_data=y, tuner='gridsearch', tuner_args=GRID_PARAMS)
```

All of those experiment would produce experiment logs in your MLflow tracking UI like below:  
![tracked experiment](/resources/images/experiment_ui.png)

## Deploy To Seldon Core  
In the Experiment instance, we also could make a deployment based on your experiment storage address. To get the experiment address, you could see it by go to your MLflow Tracking UI, select your experiments name there, and klick the desired models on the experiment id page. Then you would see this page, and copy your experiment artifact address as marked by red rectangle in below example.  
![Experiment Id Example](/resources/images/experiment_result.png)  

Add below code to deploy your experiment.
```py

from klops.seldon_core.auth import GKEAuthentication

artifact_uri = "<storage-provider>://your-bucket/mlruns/11/<your-experiment-id>/artifacts/model"
deployment_name = "Deployment Example"
model_name = "Example Model"

authentication = GKEAuthentication(
    project_id="the-project-id",
    zone="the-region",
    cluster_id="the-cluster-name")

experiment.deploy(artifact_uri=artifact_uri, deployment_name=deployment_name, model_name=model_name, authentication, namespace="your-namespace")
```

And you could access your deployed model here:
`http://<ingress_url>/seldon/<namespace>/<model-name>/api/v1.0/doc/`. Example result:  
![Deployment Example](/resources/images/deployment_result_example.jpg)