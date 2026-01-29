class PACKMOLRuntimeError(Exception):
    """Exception raised when PACKMOL fails to execute / converge."""


class PACKMOLValueError(Exception):
    """Exception raised when a bad input is passed to a PACKMOL wrapper."""
