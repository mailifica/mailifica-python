from typing import Any, Dict, List, Optional
from mailifica._client import HttpClient

class Batch:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def send(self, params: List[Dict[str, Any]]) -> Dict[str, Any]:
        return Batch.send_batch(params, api_key=self.api_key)

    @classmethod
    def send_batch(cls, params: List[Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        normalized = []
        for item in params:
            d = dict(item)
            if "from_email" in d:
                d["from"] = d.pop("from_email")
            if "from_" in d:
                d["from"] = d.pop("from_")
            if isinstance(d.get("to"), str):
                d["to"] = [d["to"]]
            if isinstance(d.get("cc"), str):
                d["cc"] = [d["cc"]]
            if isinstance(d.get("bcc"), str):
                d["bcc"] = [d["bcc"]]
            normalized.append(d)
        return HttpClient.request("POST", "/emails/batch", params=normalized, api_key=api_key)

    # Class-level static alias
    @classmethod
    def send(cls, params: List[Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        return cls.send_batch(params, api_key=api_key)
