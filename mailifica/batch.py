from typing import Any, Dict, List, Optional
from mailifica._client import HttpClient, class_or_instancemethod

class Batch:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @class_or_instancemethod
    def send(self_or_cls, params: List[Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Batch):
            key = key or self_or_cls.api_key
        return Batch.send_batch(params, api_key=key)

    @classmethod
    def send_batch(cls, params: List[Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        normalized = []
        for item in params:
            d = dict(item)
            if "from_email" in d:
                d["from"] = d.pop("from_email")
            if "from_" in d:
                d["from"] = d.pop("from_")
            if isinstance(d.get("to"), list) and len(d.get("to")) > 0:
                d["to"] = d["to"][0]
            if isinstance(d.get("cc"), str):
                d["cc"] = [d["cc"]]
            if isinstance(d.get("bcc"), str):
                d["bcc"] = [d["bcc"]]
            normalized.append(d)
        return HttpClient.request("POST", "/emails/batch", params={"emails": normalized}, api_key=api_key)
