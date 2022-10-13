"""
Seldon deployment exception handler module.
"""
from typing import Optional
from kubernetes.client import ApiException


class DeploymentException(ApiException):
    """
    Seldon Deployment Exception Class Handler.
    """

    def __init__(self, *,
                 status: Optional[int] = None, reason: Optional[str] = None, http_resp=None):
        """
        The constructor for the exception class handler.

        Args:
            status (int, optional):  Defaults to None. The exception status code.
            reason (str, optional):  Defaults to None. The exception elaborated reason.
            http_resp (_type_, optional):  Defaults to None. The HTTP response.
        """
        self.status = status
        self.reason = reason
        self.http_resp = http_resp
        self.body = http_resp.data
        self.headers = http_resp.getheaders()
        super(DeploymentException, self).__init__(
            status, reason, http_resp)
