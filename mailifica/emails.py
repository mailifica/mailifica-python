from typing import Any, Dict, List, Optional, Union
from typing_extensions import TypedDict
from mailifica._client import HttpClient, class_or_instancemethod

class Tag(TypedDict, total=False):
    name: str
    value: str

class Attachment(TypedDict, total=False):
    content: Union[str, bytes]
    filename: str
    content_type: str
    path: str

class SendParams(TypedDict, total=False):
    from_email: str
    from_: str
    to: Union[str, List[str]]
    subject: str
    html: Optional[str]
    text: Optional[str]
    cc: Optional[Union[str, List[str]]]
    bcc: Optional[Union[str, List[str]]]
    reply_to: Optional[Union[str, List[str]]]
    headers: Optional[Dict[str, str]]
    attachments: Optional[List[Attachment]]
    tags: Optional[List[Tag]]
    scheduled_at: Optional[str]

class Emails:
    SendParams = SendParams

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @class_or_instancemethod
    def send(self_or_cls, params: Union[SendParams, Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Emails):
            key = key or self_or_cls.api_key
        return Emails.send_email(params, api_key=key)

    @class_or_instancemethod
    def get(self_or_cls, email_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key
        if isinstance(self_or_cls, Emails):
            key = key or self_or_cls.api_key
        return Emails.get_email(email_id, api_key=key)

    @classmethod
    def send_email(cls, params: Union[SendParams, Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        payload = dict(params)
        if "from" in payload:
            payload["from"] = payload.pop("from")
        elif "from_email" in payload:
            payload["from"] = payload.pop("from_email")
        elif "from_" in payload:
            payload["from"] = payload.pop("from_")

        if isinstance(payload.get("to"), list):
            payload["to"] = payload["to"][0] if payload["to"] else ""
        if isinstance(payload.get("reply_to"), list):
            payload["reply_to"] = payload["reply_to"][0] if payload["reply_to"] else ""
        if isinstance(payload.get("cc"), str):
            payload["cc"] = [payload["cc"]]
        if isinstance(payload.get("bcc"), str):
            payload["bcc"] = [payload["bcc"]]

        return HttpClient.request("POST", "/emails", params=payload, api_key=api_key)

    @classmethod
    def get_email(cls, email_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", f"/emails/{email_id}", api_key=api_key)
