"""
Kubernetes authentication Basic Schema module.
"""
from abc import ABC, abstractmethod


class AbstractKubernetesAuth(ABC):
    """
    Abstract Class for Kubernetes get authentication
    """

    @abstractmethod
    def get_token(self) -> str:
        """
        Get token string from platforms.
        Returns:
            A string of Authorization token.
        """

    @abstractmethod
    def get_host(self) -> str:
        """
        Get cluster host URI from platfroms.
        Returns:
            A string of host URI.
        """
