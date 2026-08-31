from typing import Any, Dict, Optional
from mailifica._client import HttpClient

class ApiKeys:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def create(self, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", "/api-keys", params=params, api_key=api_key or self.api_key)

    def list(self, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", "/api-keys", api_key=api_key or self.api_key)

    def remove(self, api_key_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("DELETE", f"/api-keys/{api_key_id}", api_key=api_key or self.api_key)

    @classmethod
    def create_api_key(cls, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", "/api-keys", params=params, api_key=api_key)

    @classmethod
    def list_api_keys(cls, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", "/api-keys", api_key=api_key)

    @classmethod
    def remove_api_key(cls, api_key_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("DELETE", f"/api-keys/{api_key_id}", api_key=api_key)
