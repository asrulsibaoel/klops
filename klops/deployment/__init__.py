"""
The Deployment init module.
"""

from aiohttp import BasicAuth
import click

from klops.deployment.auth.default import DefaultAuthentication
from klops.deployment.auth.schema import AbstractKubernetesAuth

from .deployment import Deployment
from .auth import GKEAuthentication


@click.command()
@click.option('--docker', is_flag=True, help='Indicates the project should be built into docker image')
def build(docker):
    """_summary_

    Args:
        docker (_type_): _description_
    """
    if docker:
        print(f'Building this repo into a docker image...')
    else:
        print(f'Building this repo using default method...')


@click.command()
@click.option('--deployment_file', '-d',
              prompt='Enter the the deployment file',
              help='The deployment file contains your kubernetes \
                  configuration for seldon deployment.')
@click.option('--auth_method', '-a',
              default="default", type=click.Choice(['default', 'gke'], case_sensitive=False),
              prompt='Enter the authentication method',
              help='The authentication method to use. Default: default.')
@click.option('--cluster', '-c', default="seldon",
              prompt='Enter the cluster name', help='cluster name to be deployed.')
@click.option('--klopsrc_file', '-r', default="seldon",
              prompt='Enter the .klopsrc file', 
              help='The .klopsrc file contains your deployment configuration.')
def gke(deployment_file: str, auth_method: str, cluster: str, klopsrc_file: str):
    """Deploy our machine learning project to the GKE - seldon cluster.

    Args:
        auth_method (str): The auth method name. Must be registered first in the .klopsrc file.
        cluster (str): The cluster name to deploy. Default to 'seldon'.
    """

    # TODO: Find the klopsrc file first, then find the authentication given.
    # read the klopsrc file with given selected auth_method.
    # throw an exception if the auth_method is not available.
    # with open(klopsrc_file, 'r', encoding="utf-8") as klopsrc:
    klops_config = GKEAuthentication.read_config(
        config_title="gke", file_name=klopsrc_file)
    # if auth_method == "gke":

    # auth_instance = GKEAuthentication(
    #     project_id="koinworks-data-staging",
    #     zone="asia-southeast2",
    #     cluster_id="seldon-system-dev")

    # elif auth_method == "default":
    #     auth_instance = DefaultAuthentication(cluster_host=klops_config.get("cluster_endpoint"))
    # else:
    #     raise ValueError("Invalid auth_method.")
    deployment = Deployment(auth_instance, cluster)
    config = deployment.load_deployment_configuration(deployment_file)
    deployment.deploy(config)
