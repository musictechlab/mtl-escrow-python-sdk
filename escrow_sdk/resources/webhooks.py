from __future__ import annotations
import hmac
import hashlib
from typing import Optional


class WebhooksResource:
    def __init__(self, client):
        self._client = client

    @staticmethod
    def verify_signature(raw_body: bytes, signature: str, secret: str) -> bool:
        """Verify webhook signature (HMAC-SHA256). Adjust to match your Escrow settings."""
        mac = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
        # Accept either raw hex or prefixed formats, normalize both sides
        return mac.lower() == signature.lower().replace("sha256=", "")
