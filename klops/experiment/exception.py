"""_summary_ Experiment exception module.

Put all the exception handlers here.
"""

class ExperimentFailedException(Exception):
    """Experiment Failed Exception

    Raised when the experiment got failed.
    """

    def __init__(self, message: str, *args: object) -> None:
        """_summary_ The Experiment Failed Constructor

        Message would store the root causes.
        Args:
            message (str): _description_
        """
        self.message = message
        super(ExperimentFailedException, self).__init__(*args)

    def __str__(self):
        return self.message


class InvalidArgumentsException(ValueError):
    """_summary_ Invalid Arguments Passed

    Raised when the given arguments are invalid.
    """

    def __init__(self, message: str,*args: object) -> None:
        """_summary_ The Exception Constructor

        Args:
            message (str): _description_ message that would be displayed to the user.
        """
        self.message = message
        super(InvalidArgumentsException, self).__init__(*args)

    def __str__(self) -> str:
        return self.message


class LogMetricException(Exception):
    """Log Metric Exception

    Raised when the Logging the metrics are failed.
    """

    def __init__(self, message: str, *args: object) -> None:
        """_summary_ The Log Metric Exception Constructor

        Message would store the root causes.
        Args:
            message (str): _description_
        """
        self.message = message
        super(LogMetricException, self).__init__(*args)

    def __str__(self):
        return self.message
