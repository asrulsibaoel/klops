"""
Default Module for Authentication Implementation
"""

from .schema import AbstractKubernetesAuth


class DefaultAuthentication(AbstractKubernetesAuth):
    """
    Default Class Implementation for Kubernetes authentication.
    """

    def get_custer_endpoint(self) -> str:
        """
        Get Default Cluster Host URI endpoint
        Returns:
            A String of Basic Cluster Host URI endpoint.
        """
        return ""

    def get_token(self) -> str:
        """
        Get Default Bearer Token String.
        Returns:
            A String of Bearer Token.
        """
        return ""


__all__ = ["DefaultAuthentication"]
