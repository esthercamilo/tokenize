import time
import jwt
import requests
import fireblocks

API_KEY = "fd53f9ca-3912-4c5c-8ae5-5a08a312ffa3"  # Substitua pela sua API Key do Fireblocks
SECRET_PATH = "/home/esther/GitProjects/tokenize/backend/core/fireblocks_secret2.key"  # Substitua pelo caminho para o arquivo da chave privada

# Função para gerar o token de autenticação
def generate_token():
    with open(SECRET_PATH, 'r') as f:
        private_key = f.read()

    payload = {
        'uri': 'v1/vault/accounts_paged',
        'nonce': int(time.time() * 1000),  # Número único para evitar replay attacks
        'iat': int(time.time())  # Timestamp de quando o token foi gerado
    }

    # Gerar o token JWT
    token = jwt.encode(payload, private_key, algorithm='RS256', headers={'kid': API_KEY})
    return token

# Função para listar contas no Fireblocks
def list_vault_accounts():

    url = "https://sandbox-api.fireblocks.io/v1/vault/accounts_paged"
    token = generate_token()  # Gerar o token JWT
    headers = {
        'X-API-Key': API_KEY,
        'Authorization': f'Bearer {token}'  # Adicionar o token JWT no cabeçalho Authorization
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None

# Executa a função
if __name__ == "__main__":
    accounts = list_vault_accounts()
    if accounts:
        print("Contas do Fireblocks:")
        print(accounts)