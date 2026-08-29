from typing import Any, Dict, List, Optional, Union
from typing_extensions import TypedDict
from mailifica._client import HttpClient

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

    def send(self, params: Union[SendParams, Dict[str, Any]]) -> Dict[str, Any]:
        return Emails.send_email(params, api_key=self.api_key)

    def get(self, email_id: str) -> Dict[str, Any]:
        return Emails.get_email(email_id, api_key=self.api_key)

    @classmethod
    def send_email(cls, params: Union[SendParams, Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        payload = dict(params)
        if "from" in payload:
            payload["from"] = payload.pop("from")
        elif "from_email" in payload:
            payload["from"] = payload.pop("from_email")
        elif "from_" in payload:
            payload["from"] = payload.pop("from_")

        if isinstance(payload.get("to"), str):
            payload["to"] = [payload["to"]]
        if isinstance(payload.get("cc"), str):
            payload["cc"] = [payload["cc"]]
        if isinstance(payload.get("bcc"), str):
            payload["bcc"] = [payload["bcc"]]

        return HttpClient.request("POST", "/emails", params=payload, api_key=api_key)

    # Class-level static aliases (Resend syntax: resend.Emails.send(...))
    @classmethod
    def send(cls, params: Union[SendParams, Dict[str, Any]], api_key: Optional[str] = None) -> Dict[str, Any]:
        return cls.send_email(params, api_key=api_key)

    @classmethod
    def get(cls, email_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        return HttpClient.request("GET", f"/emails/{email_id}", api_key=api_key)
