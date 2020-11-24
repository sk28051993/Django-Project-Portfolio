from rest_framework import serializers
from trade.models import trade

class tradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = trade
        fields = ['id', 'contract_id','timeStamp','trade_date','payment_date', 'trade_side', 'trade_quantity', 'trade_price','amount','net_size','contract_size','contract_name']
