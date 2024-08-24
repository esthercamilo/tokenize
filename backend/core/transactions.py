import time
import jwt
import requests
import datetime

API_KEY = "fe0c08f7-ea1a-49ed-8076-5da79b0bc152"  # Substitua pela sua API Key do Fireblocks
SECRET_PATH = "/home/esther/GitProjects/tokenize/backend/core/fireblocks_secret4.key"  # Substitua pelo caminho para o arquivo da chave privada

# Função para gerar o token de autenticação
def generate_token():
    with open(SECRET_PATH, 'r') as f:
        private_key = f.read()

    # Usar UTC para os timestamps
    # current_time_utc = int(time.time())  # Timestamp atual em segundos, UTC
    current_time_utc = int(datetime.datetime.now().timestamp())
    nonce = int(time.time() * 1000)  # Número único em milissegundos para evitar replay attacks

    payload = {
        'uri': '/v1/vault/accounts_paged',  # Certifique-se de que o URI está correto
        'nonce': nonce,
        'iat': current_time_utc,
        'exp': 36000,
        'sub': API_KEY
    }

    # Gerar o token JWT
    try:
        token = jwt.encode(payload, private_key, algorithm='RS256', headers={'kid': API_KEY})
    except Exception as e:
        print(f"Erro ao gerar o token: {e}")
        return None

    return token

# Função para listar contas no Fireblocks
def list_vault_accounts():
    url = "https://sandbox-api.fireblocks.io/v1/vault/accounts_paged"  # URL do endpoint
    token = generate_token()  # Gerar o token JWT
    if not token:
        print("Erro ao gerar o token JWT.")
        return None

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
