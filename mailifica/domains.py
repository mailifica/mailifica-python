from typing import Any, Dict, Optional
from mailifica._client import HttpClient, class_or_instancemethod

class Domains:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @class_or_instancemethod
    def create(self_or_cls, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Domains):
            key = key or self_or_cls.api_key
        return HttpClient.request("POST", "/domains", params=params, api_key=key)

    @class_or_instancemethod
    def list(self_or_cls, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Domains):
            key = key or self_or_cls.api_key
        return HttpClient.request("GET", "/domains", api_key=key)

    @class_or_instancemethod
    def get(self_or_cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Domains):
            key = key or self_or_cls.api_key
        return HttpClient.request("GET", f"/domains/{domain_id}", api_key=key)

    @class_or_instancemethod
    def verify(self_or_cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Domains):
            key = key or self_or_cls.api_key
        return HttpClient.request("POST", f"/domains/{domain_id}/verify", api_key=key)

    @class_or_instancemethod
    def remove(self_or_cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Domains):
            key = key or self_or_cls.api_key
        return HttpClient.request("DELETE", f"/domains/{domain_id}", api_key=key)

    @classmethod
    def create_domain(cls, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", "/domains", params=params, api_key=api_key)

    @classmethod
    def list_domains(cls, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", "/domains", api_key=api_key)

    @classmethod
    def get_domain(cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", f"/domains/{domain_id}", api_key=api_key)

    @classmethod
    def verify_domain(cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", f"/domains/{domain_id}/verify", api_key=api_key)

    @classmethod
    def remove_domain(cls, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("DELETE", f"/domains/{domain_id}", api_key=api_key)
