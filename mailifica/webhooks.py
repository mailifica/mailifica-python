import hmac
import hashlib
import json
from typing import Any, Dict, Union
from mailifica.errors import InvalidRequestError

class Webhooks:
    @staticmethod
    def verify_signature(payload: Union[str, bytes], signature: str, secret: str) -> bool:
        if not signature or not secret:
            return False

        if isinstance(payload, str):
            body_bytes = payload.encode("utf-8")
        else:
            body_bytes = payload

        expected_sig = hmac.new(
            secret.encode("utf-8"),
            body_bytes,
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(signature, expected_sig)

    @classmethod
    def construct_event(cls, payload: Union[str, bytes], signature: str, secret: str) -> Dict[str, Any]:
        if not cls.verify_signature(payload, signature, secret):
            raise InvalidRequestError("Invalid webhook HMAC signature.")

        if isinstance(payload, bytes):
            payload = payload.decode("utf-8")

        return json.loads(payload)
