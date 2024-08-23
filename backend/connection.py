from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.base_path import BasePath
from fireblocks.models.create_vault_account_request import CreateVaultAccountRequest
from pprint import pprint

my_api_key="your_api_key" #I don't have any api key, please insert the one you got
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

    configuration = ClientConfiguration(
        api_key=my_api_key,
        secret_key=secret_key_value,
        base_path=BasePath.US
)
    
    
    with Fireblocks(configuration) as fireblocks:create_vault_account_request: CreateVaultAccountRequest = CreateVaultAccountRequest(
                                    name='Test Account',
                                    hidden_on_ui=False,
                                    auto_fuel=False
                                    )
    try:
        # Create a new vault account
        future = fireblocks.vaults.create_vault_account(create_vault_account_request=create_vault_account_request)
        api_response = future.result()  # Wait for the response
        print("The response of VaultsApi->create_vault_account:\n")
        pprint(api_response.data.to_json())
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)

         
    with Fireblocks(configuration) as fireblocks:create_vault_account_request: CreateVaultAccountRequest = CreateVaultAccountRequest(
                                    name='Test Account2',
                                    hidden_on_ui=False,
                                    auto_fuel=False
                                    )
    try:
        # Create a new vault account
        future = fireblocks.vaults.create_vault_account(create_vault_account_request=create_vault_account_request)
        api_response = future.result()  # Wait for the response
        print("The response of VaultsApi->create_vault_account:\n")
        pprint(api_response.data.to_json())
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)