"""
Deployment Module for Seldon Core.
"""
import json
import pathlib
from typing import Dict
import yaml

from kubernetes import client

from klops.seldon_core.auth.schema import AbstractKubernetesAuth
from klops.seldon_core.exception import SeldonDeploymentException


class SeldonDeployment:
    """
    CRUD Kubernetes operation class implementation for Seldon ML Deployment.
    """

    api: client.CustomObjectsApi = None

    def __init__(self,
                 authentication: AbstractKubernetesAuth,
                 namespace: str) -> None:
        self.authentication = authentication
        self.namespace = namespace
        self.connect_to_cluster()

    def connect_to_cluster(self) -> None:
        """
        connect_to_cluster.
        Args:
            cluster_name (str):
                String of cluster name.
        Raises:
            Exception: fff.
        """
        configuration = client.Configuration()
        configuration.host = self.authentication.get_custer_endpoint()
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = "Bearer " + \
            self.authentication.get_token()

        api_client = client.ApiClient(configuration=configuration)
        self.api = client.CustomObjectsApi(api_client=api_client)

    def load_deployment_configuration(self, file_name: str):
        """
        Load the deployment configuration file into a Python dictionary.
        Args:
            file_name (str): the deployment file name. 
            It can be Yaml file (.yml or .yaml) or JSON file.
        Returns:
            deployment_config (dict): Seldon Deployment configuration dictionary.
        Raises:
            ValueError: When the file type are not yaml or json.
            JSONDecodeError: When the JSON file contains wrong format.
            YAMLError: When the Yaml contains wrong format.
        """
        deployment_config = {}

        with open(file_name, "rb") as file:
            extension = pathlib.Path(file_name).suffix
            if extension == ".json":
                deployment_config = json.load(file)
            elif extension in [".yaml", ".yml"]:
                deployment_config = yaml.safe_load(file)
            else:
                raise ValueError("Invalid file type.")
        return deployment_config

    def deploy(self, deployment_config: Dict) -> Dict:
        """
        Deploy the ML Model
        Args:
            deployment_config (Union[object, Dict]):
                Deployment Configuration Object.
        Returns:
            deployment_result (Dict): The deployment result metadata in a dictionary.
        Raises:
            SeldonDeploymentException: Raised when the deployment failed.
        """
        deployment_name = deployment_config["metadata"]["name"]

        deployment_existence = self.check_deployment_exist(
            deployment_name=deployment_name)
        if not deployment_existence:

            deployment_result = self.api.create_namespaced_custom_object(
                group="machinelearning.seldon.io",
                version="v1alpha2",
                plural="seldondeployments",
                body=deployment_config,
                namespace=self.namespace)
        else:
            deployment_result = self.api.patch_namespaced_custom_object(
                group="machinelearning.seldon.io",
                version="v1alpha2",
                name=deployment_name,
                plural="seldondeployments",
                body=deployment_config,
                namespace=self.namespace)
        return deployment_result

    def check_deployment_exist(self, deployment_name: str) -> bool:
        """
        Check the deployment already exists.
        Args:
            deployment_name (str): The deployment name, Example: iris-model
        Returns:
            bool: The deployment existence.
        Raises:
            AttributeError: Raised when the key doesn't exists.
            NoneTypeException: Raised when wrong compared with None Object.
        """
        deployment_names = []
        response = self.api.list_namespaced_custom_object(
            group="machinelearning.seldon.io",
            version="v1alpha2",
            plural="seldondeployments",
            namespace=self.namespace)
        for item in response["items"]:
            deployment_names.append(item["metadata"]["name"])
        return deployment_name in deployment_names

    def delete(self, deployment_config: Dict) -> bool:
        """
        Deploy the ML Model
        Args:
            deployment_config (Union[object, Dict]):
                Deployment Configuration Object.
        Returns:
            bool: Boolean result of deployment deletion.
        Raises:
            SeldonDeploymentException: Raised when the deployment failed.
        """
        try:
            deployment_existence = self.check_deployment_exist(
                deployment_name=deployment_config["metadata"]["name"])
            if not deployment_existence:
                return False
            else:
                deletion_result = self.api.delete_namespaced_custom_object(
                    group="machinelearning.seldon.io",
                    version="v1alpha2",
                    name=deployment_config["metadata"]["name"],
                    plural="seldondeployments",
                    namespace=self.namespace)
                if deletion_result:
                    return True
        except SeldonDeploymentException as deployment_exception:
            print("Deployment failed,", str(deployment_exception))
            return False
