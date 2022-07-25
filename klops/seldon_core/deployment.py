"""
Testing the module.
"""
from typing import Dict, Union
from google.auth import default, compute_engine
from google.cloud.container_v1 import ClusterManagerClient
from kubernetes import client

from klops.seldon_core.auth.schema import AbstractKubernetesAuth


class SeldonDeployment:
    """
    CRUD Kubernetes operation class implementation for Seldon ML Deployment.
    """

    def __init__(self, authentication: AbstractKubernetesAuth) -> None:
        self.authentication = authentication

    def connect_to_cluster(self, cluster_name: str) -> Union[str, list, None]:
        """
        connect_to_cluster.
        Args:
            cluster_name (str):
                String of cluster name.
        Raises:
            Exception: fff.
        """
    
    def deploy(self, deployment_config: Union[object, Dict]) -> bool:
        """
        Deploy the ML Model
        Args:
            deployment_config (Union[object, Dict]):
                Deployment Configuration Object.
        Raises:
            Exception: ddd.
        """


def test_gke(project_id: str, zone: str, cluster_id: str):
    """
    Testing the GKE
    """
    try:
        # credentials = compute_engine.Credentials(service_account_email="931158784113-compute@developer.gserviceaccount.com")
        # print(credentials.__dict__)

        cluster_manager_client = ClusterManagerClient()
        cluster = cluster_manager_client.get_cluster(
            name=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}')

        print("Cluster endpoint", cluster.endpoint)
    except Exception as exception:
        print(str(exception))

    configuration = client.Configuration()
    configuration.host = f"https://{cluster.endpoint}:443"
    configuration.verify_ssl = False
    configuration.api_key_prefix["authorization"] = "Bearer"
    configuration.api_key['authorization'] = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkhKYUdkV2QyVTAtSE5SWGtfQ1BNOXE0WndrRUplRjRQWC1HaUg3U3k5LWcifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4teDl3czciLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjUzNzAxZjUyLTMwZjMtNGNjMC1hYjc4LWM2YzdhYWRjZTdkYiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.oqs1HDgUJexcMY5LqkIZAWAqQ1KhAZGmh1Y3xXZ8o3m5skhV8Cgr_FYGPa_jp6WbPast0PZu4kpP9q18QFys51diEj5MsND4M7zdpwABSqcyEpqDEm8X_37WIyq4McGXjmrc247LoqirJCBoUR7N36LFh6LQYlj9rRVh7ac5m1gjKihrMRKIFTRaPLV1zFZ71c6Ds_9Cezxpaz8XhOutJPAeoyBD8EfWZlD9-S6Q-JF8-GH3G2k9oaIcbqz88CqO_qMSyX_lWhZor-sz7iNg4yB1ePd1pdvPwMjTc4HAL450zIhRi95dCBmlYvYlEjkjnr5HlArwDUZEo5EKJRfYYQ"
    client.Configuration.set_default(configuration)

    v1_api = client.CoreV1Api()
    print("Listing pods with their IPs:")
    pods = v1_api.list_pod_for_all_namespaces(watch=False)
    for i in pods.items:
        print(f"{i.status.pod_ip}, {i.metadata.namespace}, {i.metadata.name}")


# ## Deploy test 2

# import googleapiclient.discovery
# from tempfile import NamedTemporaryFile
# import kubernetes
# import base64

# def token(*scopes):
#     credentials = googleapiclient._auth.default_credentials()
#     scopes = [f'https://www.googleapis.com/auth/{s}' for s in scopes]
#     scoped = googleapiclient._auth.with_scopes(credentials, scopes)
#     googleapiclient._auth.refresh_credentials(scoped)
#     return scoped.token

# def kubernetes_api(cluster):
#     config = kubernetes.client.Configuration()
#     config.host = f'https://{cluster["endpoint"]}'

#     config.api_key_prefix['authorization'] = 'Bearer'
#     config.api_key['authorization'] = token('cloud-platform')

#     with NamedTemporaryFile(delete=False) as cert:
#         cert.write(base64.decodebytes(cluster['masterAuth']['clusterCaCertificate'].encode()))
#         config.ssl_ca_cert = cert.name

#     client = kubernetes.client.ApiClient(configuration=config)
#     api = kubernetes.client.CoreV1Api(client)

#     return api

# def run(cluster):
#     """You'll need to give whichever account `googleapiclient` is using the 
#     'Kubernetes Engine Developer' role so that it can access the Kubernetes API.

#     `cluster` should be the dict you get back from `projects.zones.clusters.get`
#     and the like"""

#     api = kubernetes_api(cluster)
#     print(api.list_pod_for_all_namespaces())

if __name__ == "__main__":
    test_gke(
        # "931158784113-compute@developer.gserviceaccount.com",
        "koinworks-data-staging",
        "asia-southeast2",
        "seldon-system-dev")
    # run()
