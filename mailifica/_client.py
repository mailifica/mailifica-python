import os
import requests
from typing import Any, Dict, Optional
from mailifica.errors import (
    MailificaError,
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    InternalServerError,
)

DEFAULT_BASE_URL = "https://api.mailifica.com/v1"

class HttpClient:
    @staticmethod
    def get_api_key(api_key: Optional[str] = None) -> str:
        from mailifica import api_key as global_key
        key = api_key or global_key or os.environ.get("MAILIFICA_API_KEY")
        if not key:
            raise AuthenticationError("No API key provided. Set mailifica.api_key or pass api_key parameter.")
        return key

    @staticmethod
    def get_base_url(base_url: Optional[str] = None) -> str:
        from mailifica import api_url as global_url
        return (base_url or global_url or os.environ.get("MAILIFICA_BASE_URL", DEFAULT_BASE_URL)).rstrip("/")

    @classmethod
    def request(
        cls,
        method: str,
        path: str,
        params: Optional[Any] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        key = cls.get_api_key(api_key)
        url = f"{cls.get_base_url(base_url)}/{path.lstrip('/')}"

        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "mailifica-python/1.0.0",
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                json=params if method in ["POST", "PUT", "PATCH", "DELETE"] and params is not None else None,
                params=params if method == "GET" and isinstance(params, dict) else None,
                headers=headers,
                timeout=30,
            )

            if not response.ok:
                try:
                    err_json = response.json()
                    message = (
                        err_json.get("error", {}).get("message")
                        if isinstance(err_json.get("error"), dict)
                        else err_json.get("message") or response.text
                    )
                    err_type = (
                        err_json.get("error", {}).get("code")
                        if isinstance(err_json.get("error"), dict)
                        else err_json.get("error")
                    )
                except Exception:
                    message = response.text
                    err_type = "unknown_error"

                if response.status_code == 401 or response.status_code == 403:
                    raise AuthenticationError(message, status_code=response.status_code, error_type=err_type)
                elif response.status_code == 400 or response.status_code == 422:
                    raise InvalidRequestError(message, status_code=response.status_code, error_type=err_type)
                elif response.status_code == 429:
                    raise RateLimitError(message, status_code=429, error_type=err_type)
                elif response.status_code >= 500:
                    raise InternalServerError(message, status_code=response.status_code, error_type=err_type)
                else:
                    raise MailificaError(message, status_code=response.status_code, error_type=err_type)

            if response.status_code == 204 or not response.content:
                return {"success": True}

            return response.json()
        except requests.RequestException as e:
            raise MailificaError(f"Network error: {str(e)}")
