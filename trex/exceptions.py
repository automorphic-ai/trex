class InvalidConfigError(Exception):
    """Raised when a CFG is invalid."""
    pass

class InvalidAPIKey(Exception):
    """Raised when an invalid API key is used."""
    pass

class InvalidJSONError(Exception):
    """Raised when the generated JSON is invalid."""
    pass