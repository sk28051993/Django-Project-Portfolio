from django.shortcuts import render
from rest_framework import viewsets

from django.shortcuts import render, get_object_or_404
from contract.models import Contract
from contract.serializers import ContractSerializer

# Create your views here.

def get_data(request):
    data = Contract.objects.all()
    return render(request, 'contract.html')

def update_data(request):
    return render(request, 'contract_update.html')

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
