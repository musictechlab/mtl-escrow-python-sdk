from __future__ import annotations

import base64
import os
from typing import Any, Dict, Optional
from dotenv import load_dotenv
import httpx

from .exceptions import EscrowAPIError, EscrowAuthError
from .resources.customers import CustomersResource
from .resources.transactions import TransactionsResource
from .resources.webhooks import WebhooksResource

load_dotenv()


class KeyAuth(httpx.Auth):
    """Attach Escrow API key using HTTP Basic auth (email as username, API key as password)."""

    def __init__(self, email: str, api_key: str):
        self.email = email
        self.api_key = api_key

    def auth_flow(self, request: httpx.Request):
        # Use HTTP Basic auth with email as username and API key as password
        token = base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        request.headers["Authorization"] = f"Basic {token}"
        yield request


class BasicAuth(httpx.Auth):
    def __init__(self, email: str, password: str):
        token = base64.b64encode(f"{email}:{password}".encode()).decode()
        self.header = f"Basic {token}"

    def auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = self.header
        yield request


class EscrowAPIClient:
    def __init__(
        self,
        api_base: str = os.getenv("ESCROW_API_BASE", "https://api.escrow-sandbox.com"),
        api_version: str = os.getenv("ESCROW_API_VERSION", "2017-09-01"),
        api_key: Optional[str] = os.getenv("ESCROW_API_KEY", None),
        email: Optional[str] = os.getenv("ESCROW_EMAIL", None),
        password: Optional[str] = os.getenv("ESCROW_PASSWORD", None),
        auth: Optional[httpx.Auth] = None,
        timeout: Optional[float] = 30.0,
        transport: Optional[httpx.BaseTransport] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.api_base = api_base.rstrip("/")
        self.api_version = api_version.strip("/")
        self.base_path = f"{self.api_base}/{self.api_version}"

        if auth:
            self.auth = auth
        elif api_key and email:
            self.auth = KeyAuth(email, api_key)
        elif email and password:
            self.auth = BasicAuth(email, password)
        else:
            raise EscrowAuthError(
                "Provide either (email + api_key) or (email + password) or a custom httpx.Auth."
            )

        self._client = httpx.Client(
            base_url=self.base_path,
            auth=self.auth,
            timeout=timeout,
            transport=transport,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                **(headers or {}),
            },
        )

        # print(self.auth)
        # print(self._client.base_url)
        # print(self._client.auth)
        # print(self._client.timeout)
        # print(self._client.transport)
        # print(self._client.headers)
        # resources
        self.customers = CustomersResource(self)
        self.transactions = TransactionsResource(self)
        self.webhooks = WebhooksResource(self)

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Dict[str, Any] | None = None,
        json: Any | None = None,
    ) -> Any:
        """Relative request against the versioned base path."""
        r = self._client.request(method, path, params=params, json=json)
        if r.status_code >= 400:
            try:
                payload = r.json()
            except Exception:
                payload = r.text
            raise EscrowAPIError(
                r.status_code, getattr(r, "reason_phrase", "Error"), payload
            )
        if r.headers.get("Content-Type", "").startswith("application/json"):
            return r.json()
        return r.text

    def _request_abs(
        self,
        method: str,
        absolute_path: str,
        *,
        params: Dict[str, Any] | None = None,
        json: Any | None = None,
    ):
        """Absolute request under same domain (e.g., /api/TransactionAction/*)."""
        url = f"{self.api_base.rstrip('/')}{absolute_path}"
        r = self._client.request(method, url, params=params, json=json)
        if r.status_code >= 400:
            try:
                payload = r.json()
            except Exception:
                payload = r.text
            raise EscrowAPIError(
                r.status_code, getattr(r, "reason_phrase", "Error"), payload
            )
        if r.headers.get("Content-Type", "").startswith("application/json"):
            return r.json()
        return r.text

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
