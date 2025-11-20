"""Custom exceptions for the Cloudpepper SDK."""


class CloudpepperError(Exception):
    """Base exception for all Cloudpepper SDK errors."""

    def __init__(self, message: str, status_code: int = None, response=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response


class AuthenticationError(CloudpepperError):
    """Raised when authentication fails (401 Unauthorized)."""


class PermissionError(CloudpepperError):
    """Raised when the user lacks permissions (403 Forbidden)."""


class NotFoundError(CloudpepperError):
    """Raised when a resource is not found (404 Not Found)."""


class ValidationError(CloudpepperError):
    """Raised when request validation fails (400 Bad Request)."""


class RateLimitError(CloudpepperError):
    """Raised when rate limit is exceeded (429 Too Many Requests)."""


class ServerError(CloudpepperError):
    """Raised when the server encounters an error (5xx)."""


class APIError(CloudpepperError):
    """Raised for other API errors."""
