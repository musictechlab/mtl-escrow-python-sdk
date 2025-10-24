class EscrowError(Exception):
    """Base error for the SDK."""


class EscrowAuthError(EscrowError):
    """Authentication/authorization problems."""


class EscrowAPIError(EscrowError):
    """Non-2xx response from API."""

    def __init__(self, status_code: int, message: str, payload=None):
        super().__init__(f"[{status_code}] {message}")
        self.status_code = status_code
        self.payload = payload
