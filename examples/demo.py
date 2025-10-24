import os

from escrow_sdk import EscrowAPIClient
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.getenv("ESCROW_API_KEY")
    email = os.getenv("ESCROW_EMAIL")
    client = EscrowAPIClient(api_key=api_key, email=email)
    print(client.customers.get_me())


if __name__ == "__main__":
    main()
