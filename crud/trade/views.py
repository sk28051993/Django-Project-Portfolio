
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from django.shortcuts import render, get_object_or_404
from trade.models import trade
from trade.serializers import tradeSerializer

# Create your views here.

def get_data(request):
    data = trade.objects.all()
    return render(request, 'trade.html')

def update_data(request):
    return render(request, 'trade_update.html')

class tradeViewSet(viewsets.ModelViewSet):
    queryset = trade.objects.all()
    serializer_class = tradeSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
