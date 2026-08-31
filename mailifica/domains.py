from typing import Any, Dict, Optional
from mailifica._client import HttpClient

class Domains:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def create(self, params: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", "/domains", params=params, api_key=api_key or self.api_key)

    def list(self, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", "/domains", api_key=api_key or self.api_key)

    def get(self, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", f"/domains/{domain_id}", api_key=api_key or self.api_key)

    def verify(self, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("POST", f"/domains/{domain_id}/verify", api_key=api_key or self.api_key)

    def remove(self, domain_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("DELETE", f"/domains/{domain_id}", api_key=api_key or self.api_key)

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
