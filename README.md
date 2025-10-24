# MTL Escrow Python SDK

**Unofficial**, lightweight Python SDK for the [Escrow.com API](https://www.escrow.com/api/docs/reference)

> ⚠️ This is a minimal client intended for prototyping.  
> Verify auth & payloads with your Escrow.com account/docs before using in production.

![Demo](demo.png)

---

## 🧩 Install

```bash
pip install mtl-escrow-python-sdk
# or from source
poetry add mtl-escrow-python-sdk
```

---

## 🛠️ Development

```bash
poetry install
poetry run black .
poetry run autopep8 --in-place --recursive .
poetry run flake8
poetry run pytest -v
```

---

## 🚀 Quickstart

### Running the Example

1. **Install dependencies:**

   ```bash
   poetry install
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root:

   ```bash
   echo "ESCROW_API_KEY=your_api_key_here" > .env
   echo "ESCROW_EMAIL=your_email@example.com" >> .env
   ```

   Replace `your_api_key_here` with your actual Escrow.com API key and `your_email@example.com` with your Escrow.com email address.

3. **Run the example:**

   ```bash
   poetry run python examples/demo.py
   ```

   The example will output a nicely formatted JSON response with your customer information:

   ```json
   {
     "address": {
       "city": "My City",
       "country": "PL",
       "line1": "Wadowicka 43",
       "post_code": "30-214",
       "state": "Małopolskie"
     },
     "company": {
       "address": {},
       "company_name": ""
     },
     "customer_email_verification": {
       "verified": false
     },
     "date_of_birth": "1982-03-10T00:00:00",
     "display_name": "Mariusz Admin",
     "electronic_verification": {
       "available": false,
       "documents_supported": []
     },
     "email": "test@musictechlab.io",
     "first_name": "Mariusz",
     "id": 3813415,
     "last_name": "Admin",
     "phone_number": "+487232473274",
     "shipping_address": {},
     "tax_numbers": [
       {
         "id": 29919,
         "number": "PL4342947811",
         "type": "vat"
       }
     ],
     "verification": {
       "company": {
         "status": "not_required"
       },
       "extended": {
         "status": "not_required"
       },
       "personal": {
         "status": "verified"
       }
     }
   }
   ```

## 🔐 Auth

- **Preferred** → API Key with HTTP Basic — pass `email` & `api_key` to use HTTP Basic authentication with email as username and API key as password.

- **Fallback** → HTTP Basic — pass `email` & `password` to send standard Basic auth.

- You can also inject a pre-configured `httpx.Auth` via the `auth=` parameter.

---

## ⚙️ Features (MVP)

- **Customers** → get self/any, list API keys  
- **Transactions** → create/get/list, perform simple actions, payment link (credit card / PayPal / wire), web action link  
- **Webhooks** → verify signature helper (HMAC-SHA256; adjust to your setup)

---

## 🧠 Notes

- Endpoints follow Escrow.com API v2017-09-01 (`/2017-09-01/transaction`, etc.).  
- This SDK focuses on simplicity and clarity — PRs are welcome for more endpoints!

---

## 📚 Learn More

- [Escrow.com API Basics](https://www.escrow.com/api/docs/basics)
- [Escrow.com API Reference](https://www.escrow.com/api/docs/reference)
- [MusicTech Lab](https://musictechlab.com)

---

## 🪪 License

MIT License — © 2025 **MusicTech Lab**  
Built with ❤️ by MusicTech Lab.
