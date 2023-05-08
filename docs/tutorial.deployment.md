# Klops Deployment  
Klops Deployment is a module to deploy the development machine learning projects into Seldon Core instance. Currently we only supports for local cluster and Google Kubernetes Engine (GKE) as the authentication to deploy. Below is the example on how to done with.

## Using Default Authentication  
```py
from klops.seldon_core import SeldonDeployment
from klops.seldon_core.auth import DefaultAuthentication

default_auth = DefaultAuthentication(
    host="<your-host-IP-or-domain>",
    token="your-secret-token")
deployment = SeldonDeployment(default_auth, "your-kubernetes-namespace")

## load your deployment config. It can be json or yaml/yml file.
config = deployment.load_deployment_configuration("<deployment-config>.json")
deployment.deploy(config)
```

## Using Google Kubernetes Engine as Authentication

```py
from klops.seldon_core import SeldonDeployment
from klops.seldon_core.auth import GKEAuthentication

gke = GKEAuthentication(
    project_id="your-project-id",
    zone="your-cluster-zone",
    cluster_id="your-cluster-id")
deployment = SeldonDeployment(gke, "your-kubernetes-namespace")

## load your deployment config. It can be json or yaml/yml file.
config = deployment.load_deployment_configuration("<deployment-config>.json")
deployment.deploy(config)
```

Now you can access your API through this URL `http://<ingress_url>/seldon/<namespace>/<model-name>/api/v1.0/doc/`. Example result:  
![Deployment Example](/resources/images/deployment_result_example.jpg)
