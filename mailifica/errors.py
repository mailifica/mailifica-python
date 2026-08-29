from typing import Optional

class MailificaError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None, error_type: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_type = error_type

class AuthenticationError(MailificaError):
    pass

class InvalidRequestError(MailificaError):
    pass

class RateLimitError(MailificaError):
    pass

class InternalServerError(MailificaError):
    pass
