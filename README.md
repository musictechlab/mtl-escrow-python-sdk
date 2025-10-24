# mtl-escrow-python-sdk

**Unofficial**, lightweight Python SDK for the Escrow.com API

> ⚠️ This is a minimal client intended for prototyping. Verify auth & payloads with your Escrow.com account/docs before production.

## Install

```bash
pip install escrow-sdk-python
# or from source
poetry add escrow-sdk-python
```

## Quickstart

```python
from escrow_sdk import EscrowAPIClient

client = EscrowAPIClient(
    api_base="https://api.escrow-sandbox.com/2017-09-01/",
    api_version="2017-09-01",
    # Option A: API key in the form "id;secret"
    api_key="113;YOUR_SECRET",
    # Option B (fallback): HTTP Basic using email/password
    # email="you@example.com", password="..."
)

me = client.customers.get_me()
print(me)

# Create a simple transaction (buyer/seller emails must be registered with Escrow)
tx = client.transactions.create({
    "currency": "usd",
    "description": "Demo purchase",
    "items": [{
        "description": "Service / goods",
        "schedule": [{"amount": 10000, "payer_customer": "buyer", "beneficiary_customer": "seller"}]
    }],
    "parties": [
        {"customer": "buyer@example.com", "role": "buyer"},
        {"customer": "seller@example.com", "role": "seller"}
    ]
})
print(tx["id"])

# Get a web action URL (e.g., to agree/fund via web)
link = client.transactions.web_link(transaction_id=tx["id"], action="agree")
print(link["url"])
```

## Auth

- Preferred: API Key header — pass `api_key="id;secret"`. The client sends `Authorization: Key id;secret`.
- Fallback: HTTP Basic — pass `email` & `password` to send standard Basic auth.
- You can also inject a pre-configured `httpx.Auth` via `auth=`.

## Features (MVP)

- Customers: get self/any, list API keys
- Transactions: create/get/list, perform simple actions, payment link (credit card / PayPal / wire), web action link
- Webhooks: verify basic signature helper (HMAC-SHA256, optional; adjust to your setup)

## Notes

- Endpoints follow Escrow.com v2017-09-01 patterns (e.g. `/2017-09-01/transaction`). See official docs.
- This package aims for simple, explicit methods; PRs welcome for more endpoints.

## 📚 Learn More

- [Escrow.com API Basics](https://www.escrow.com/api/docs/basics)
- [Escrow.com API Reference](https://www.escrow.com/api/docs/reference)
- [MusicTech Lab](https://musictechlab.com)

## 🪪 License

MIT License — © 2025 MusicTech Lab.
Built with ❤️ by MusicTech Lab.
