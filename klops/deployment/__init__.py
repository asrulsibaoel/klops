"""
The Deployment init module.
"""

import click
from .deployment import Deployment


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
@click.option('--env', '-e',
              default="dev", type=click.Choice(['dev', 'stg', 'prd'], case_sensitive=False),
              prompt='Enter env name to deploy', help='Env to deploy')
@click.option('--cloud', '-c', default="aws",
              type=click.Choice(['aws', 'gcp', 'azure'],case_sensitive=False),
              prompt='Enter cloud to deploy to', help='Cloud to deploy to')
def deploy(env: str, cloud: str):
    """Deploy our machine learning project to the seldon cluster.

    Args:
        env (str): the environment name.
        cloud (str): _description_
    """

    print(
        f'Deploying current application artifact to {env} environment in {cloud} cloud...')
