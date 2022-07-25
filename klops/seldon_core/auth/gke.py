"""
Google Kubernetes Engine (GKE) Module for Authentication Implementation
"""

from .schema import AbstractKubernetesAuth


class GKEAuthentication(AbstractKubernetesAuth):
    """
    Google Kubernetes Engine (GKE) Class Implementation for Kubernetes authentication.
    """

    def get_host(self) -> str:
        """
        Get GKE Cluster Host
        Returns:
            A String of GKE Cluster Host URI.
        """
        return ""

    def get_token(self) -> str:
        """
        Get GKE Bearer Token String.
        Returns:
            A String of GKE Bearer Token String.
        """
        return ""

