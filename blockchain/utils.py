try:
    import os
    import solcx

    # Verifica se o solc está instalado, caso não esteja, tenta instalá-lo
    try:
        compiler_version = solcx.get_solc_version()
        print(f"Found solc compiler version {compiler_version}")
    except Exception as e:
        print(f"solc is not installed or another error {e}")
        solcx.install_solc()

    from web3 import Web3

    solcx.set_solc_version('0.8.26')
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contract_path = os.path.join(BASE_DIR, 'blockchain/contracts/EvaluationPlatform.sol')

    with open(contract_path, 'r') as file:
        contract_source_code = file.read()

    compiled_sol = solcx.compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:EvaluationPlatform']

    EvaluationPlatform = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )


    def deploy_contract():
        tx_hash = EvaluationPlatform.constructor().transact({'from': w3.eth.accounts[0]})
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt.contractAddress


    def get_contract_instance(address):
        return w3.eth.contract(address=address, abi=contract_interface['abi'])
except Exception as e:
    print(e)
    print('Na MVP camada de blockchain foi substituída por um banco sqlite')
