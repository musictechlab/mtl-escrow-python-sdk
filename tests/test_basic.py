import pytest
from escrow_sdk import EscrowAPIClient
from escrow_sdk.exceptions import EscrowAuthError


def test_auth_error_when_no_credentials():
    """Client should raise error when no auth provided."""
    with pytest.raises(EscrowAuthError):
        EscrowAPIClient(api_key=None, email=None, password=None)


def test_client_has_resources():
    """Client exposes expected resources."""
    client = EscrowAPIClient(api_key="id;secret", api_base="https://example.com")
    assert hasattr(client, "customers")
    assert hasattr(client, "transactions")
    assert hasattr(client, "webhooks")
    client.close()


def test_request_abs_url_build(monkeypatch):
    """Ensure _request_abs forms correct URL and calls httpx.Client.request()."""
    called = {}

    def fake_request(method, url, **kwargs):
        called.update(dict(method=method, url=url))

        class Resp:
            status_code = 200
            headers = {"Content-Type": "application/json"}

            def json(self):
                return {"ok": True}

        return Resp()

    client = EscrowAPIClient(api_key="1;2", api_base="https://sandbox.escrow.com")
    monkeypatch.setattr(client._client, "request", fake_request)
    result = client._request_abs("GET", "/api/test")
    assert result == {"ok": True}
    assert called["url"] == "https://sandbox.escrow.com/api/test"
