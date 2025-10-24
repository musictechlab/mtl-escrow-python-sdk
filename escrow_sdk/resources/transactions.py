from __future__ import annotations
from typing import Any, Dict


class TransactionsResource:
    def __init__(self, client):
        self._client = client

    def create(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """POST /{version}/transaction"""
        return self._client._request("POST", "/transaction", json=body)

    def get(self, transaction_id: int | str) -> Dict[str, Any]:
        """GET /{version}/transaction/{transaction_id}"""
        return self._client._request("GET", f"/transaction/{transaction_id}")

    def list(self, *, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        """GET /{version}/transaction?page=...&page_size=..."""
        return self._client._request(
            "GET", "/transaction", params={"page": page, "page_size": page_size}
        )

    def agree(self, transaction_id: int | str) -> Dict[str, Any]:
        """POST /api/TransactionAction/agree — mark agreement for the current party."""
        body = {"transaction_id": int(transaction_id)}
        return self._client._request_abs(
            "POST", "/api/TransactionAction/agree", json=body
        )

    def payment_link(
        self, transaction_id: int | str, payment_method: str
    ) -> Dict[str, Any]:
        """POST /{version}/transaction/{transaction_id}/payment_methods/{payment_method}"""
        return self._client._request(
            "POST", f"/transaction/{transaction_id}/payment_methods/{payment_method}"
        )

    def web_link(self, transaction_id: int | str, action: str) -> Dict[str, Any]:
        """GET /{version}/transaction/{transaction_id}/web_link/{action}"""
        return self._client._request(
            "GET", f"/transaction/{transaction_id}/web_link/{action}"
        )
