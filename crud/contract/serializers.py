from rest_framework import serializers
from contract.models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'contract_name', 'contract_type', 'contract_size', 'contract_startDate', 'contract_endDate', 'frequency','contract_priceType', 'created', 'updated' ]
