"""
Seldon deployment exception handler module.
"""
from kubernetes.client import ApiException


class SeldonDeploymentException(ApiException):
    """
    Seldon Deployment Exception Class Handler.
    """

    def __init__(self, *, status=None, reason=None, http_resp=None):
        """_summary_

        Args:
            status (_type_, optional): _description_. Defaults to None. The exception status code.
            reason (_type_, optional): _description_. Defaults to None. The exception elaborated reason.
            http_resp (_type_, optional): _description_. Defaults to None. The HTTP response.
        """
        super(SeldonDeploymentException, self).__init__(status, reason, http_resp)
