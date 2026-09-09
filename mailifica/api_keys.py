from typing import Any, Dict, Optional
from mailifica._client import HttpClient, class_or_instancemethod

class ApiKeys:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @class_or_instancemethod
    def create(self_or_cls, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, ApiKeys):
            key = key or self_or_cls.api_key
        return HttpClient.request("POST", "/api-keys", params=params, api_key=key)

    @class_or_instancemethod
    def list(self_or_cls, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, ApiKeys):
            key = key or self_or_cls.api_key
        return HttpClient.request("GET", "/api-keys", api_key=key)

    @class_or_instancemethod
    def remove(self_or_cls, api_key_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, ApiKeys):
            key = key or self_or_cls.api_key
        return HttpClient.request("DELETE", f"/api-keys/{api_key_id}", api_key=key)

    @classmethod
    def create_api_key(cls, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", "/api-keys", params=params, api_key=api_key)

    @classmethod
    def list_api_keys(cls, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", "/api-keys", api_key=api_key)

    @classmethod
    def remove_api_key(cls, api_key_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("DELETE", f"/api-keys/{api_key_id}", api_key=api_key)
