import requests
import jwt  # type: ignore
import time
import json

API_BASE_URL = "https://api.fireblocks.io/v1"
API_KEY = "your_api_key"  # Replace with the fireblocks api Key
SECRET_PATH = "path/to/your_private_key.pem"  # Replace with the path to the private key file

# Function to generate JWT token
def generate_jwt(api_key, secret_path):
    with open(secret_path, "r") as key_file:
        private_key = key_file.read()
    
    headers = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": api_key
    }
    
    payload = {
        "nonce": int(time.time() * 1000),
        "iat": int(time.time())
    }
    
    token = jwt.encode(payload, private_key, algorithm='RS256', headers=headers)
    return token

# Function to create a token transaction
def create_token_transaction(api_key, secret_path, source_vault_account_id, destination_address, amount, asset_id, gas_limit, gas_price):
    jwt_token = generate_jwt(api_key, secret_path)
    
    headers = {
        "X-API-Key": api_key,
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "assetId": asset_id,  # Example: "ETH"
        "source": {
            "type": "VAULT_ACCOUNT",
            "id": source_vault_account_id  # Replace with the vault account ID
        },
        "destination": {
            "type": "ONE_TIME_ADDRESS",
            "oneTimeAddress": {
                "address": destination_address,  # Replace with the recipient's address
                "tag": "",  # Only for certain blockchains (e.g., XRP, XLM)
                "destination": "",
                "destinationTag": "",
                "label": "Recipient Name"
            }
        },
        "amount": str(amount),  # Amount to transfer
        "fee": "",
        "gasLimit": gas_limit,  # Optional: for Ethereum transactions
        "gasPrice": gas_price,  # Optional: for Ethereum transactions
        "networkFee": "",
        "externalTxId": "",
        "note": "Token transaction via Fireblocks API"
    }
    
    response = requests.post(f"{API_BASE_URL}/transactions", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("Transaction created successfully:", response.json())
    else:
        print("Error:", response.status_code, response.text)

source_vault_account_id = "Test Account"
destination_address = "Test Account2"
amount = 0.01  # Amount of tokens to send
asset_id = "ETH"  # Token type
gas_limit = 21000  # Typical gas limit for a simple ETH transfer
gas_price = 50  # Gwei

create_token_transaction(API_KEY, SECRET_PATH, source_vault_account_id, destination_address, amount, asset_id, gas_limit, gas_price)