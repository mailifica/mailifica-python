import os
from typing import Optional
from mailifica.emails import Emails
from mailifica.batch import Batch
from mailifica.domains import Domains
from mailifica.api_keys import ApiKeys
from mailifica.webhooks import Webhooks
from mailifica.errors import (
    MailificaError,
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    InternalServerError,
)
from mailifica._version import __version__

api_key: Optional[str] = os.environ.get("MAILIFICA_API_KEY")
api_url: Optional[str] = os.environ.get("MAILIFICA_BASE_URL")

class Mailifica:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("MAILIFICA_API_KEY")
        self.emails = Emails(api_key=self.api_key)
        self.batch = Batch(api_key=self.api_key)
        self.domains = Domains(api_key=self.api_key)
        self.api_keys = ApiKeys(api_key=self.api_key)
        self.webhooks = Webhooks()

__all__ = [
    "Mailifica",
    "Emails",
    "Batch",
    "Domains",
    "ApiKeys",
    "Webhooks",
    "MailificaError",
    "AuthenticationError",
    "InvalidRequestError",
    "RateLimitError",
    "InternalServerError",
    "api_key",
    "api_url",
    "__version__",
]
