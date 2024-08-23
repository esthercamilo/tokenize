from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import User
from api.serializers import UserSerializer


try:
    from blockchain.utils import deploy_contract, get_contract_instance, w3
    contract_address = deploy_contract()
    contract = get_contract_instance(contract_address)
except Exception as e:
    print(e)
    print("Utilização de contratos somente na V1")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_data = response.data

        # A ser implementado na V1
        # account = w3.eth.accounts[0]
        # tx_hash = contract.functions.addUser(user_data['name']).transact({'from': account})
        # w3.eth.wait_for_transaction_receipt(tx_hash)

        return response
