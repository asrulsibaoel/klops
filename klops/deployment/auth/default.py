"""
Default Module for Authentication Implementation
"""

from typing import Any
from .schema import AbstractKubernetesAuth


class DefaultAuthentication(AbstractKubernetesAuth):
    """
    Default Class Implementation for Kubernetes authentication.
    """

    def __init__(self,
                 cluster_host: str = "localhost",
                 token: str = "TokenString123",
                 **kwargs: Any) -> None:
        """
        Default Class Implementation for Kubernetes authentication.
        Args:
            cluster_host (str, optional):  Defaults to "localhost".
            token (str, optional):  Defaults to "TokenString123".
        """
        self.cluster_host = cluster_host
        self.token = token
        super(DefaultAuthentication, self).__init__(**kwargs)

    def get_custer_endpoint(self) -> str:
        """
        Get Default Cluster Host URI endpoint.

        Returns:
            str: A string of Basic Cluster Host URI endpoint.
        """
        return f"https://{self.cluster_host}:443"

    def get_token(self) -> str:
        """
        Get Default Bearer Token String.
        Returns:
            str: A string of Bearer Token.
        """
        return self.token



__all__ = ["DefaultAuthentication"]
