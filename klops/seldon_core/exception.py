"""
Seldon deployment exception handler module.
"""
from kubernetes.client import ApiException


class SeldonDeploymentException(ApiException):
    """
    Seldon Deployment Exception Class Handler.
    """

    def __init__(self, *, status=None, reason=None, http_resp=None):
        super(SeldonDeploymentException, self).__init__(status, reason, http_resp)
