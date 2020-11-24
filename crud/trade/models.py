
from django.db import models

from django.utils import timezone
# Create your models here.
from contract.models import Contract
class trade(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE,default=14)
    timeStamp = models.DateTimeField(default=timezone.now)
    trade_date = models.DateField(default=timezone.now)
    payment_date = models.DateField(default=timezone.now)
    trade_side=models.CharField(max_length=100,default='Buy')
    trade_quantity = models.IntegerField(default=0)
    trade_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)
    net_size = models.IntegerField(default=1)
    contract_size = models.IntegerField(default=1)
    contract_name = models.CharField(max_length=100,default = 'contract1')

     


    # contract_id = models.ForeignKey(contract, on_delete=models.CASCADE)
    # loginUserId = models.ForeignKey(User, on_delete=models.CASCADE)
    # timeStamp = models.DateTimeField(default=timezone.now)
    # trade_date = models.DateField()
    # payment_date = models.DateField()
    # trade_side=models.CharField(max_length=100)
    # trade_quantity = models.IntegerField()
    # counterpary_id = models.ForeignKey(CounterParty, on_delete=models.CASCADE,default=1)
    # trade_price = models.IntegerField(default=1)
    # amount = models.IntegerField(default=1)
    # net_size = models.IntegerField(default=1)
    # contract_size = models.IntegerField(default=1)
    # contract_name = models.CharField(max_length=100,default = 'contract1')
    # counterparty_name = models.CharField(max_length=100,default = 'EDF')
