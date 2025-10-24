from __future__ import annotations
from typing import Any, Dict, Optional


class CustomersResource:
    def __init__(self, client):
        self._client = client

    def get_me(self):
        """GET /{version}/customer/me"""
        return self._client._request("GET", "/customer/me")  # /2017-09-01/customer/me

    def get(self, customer_id: int | str):
        """GET /{version}/customer/{customer_id} or 'me'"""
        return self._client._request("GET", f"/customer/{customer_id}")

    def api_keys(self, customer_id: int | str = "me"):
        """GET /{version}/customer/{customer_id}/api_key"""
        return self._client._request("GET", f"/customer/{customer_id}/api_key")
