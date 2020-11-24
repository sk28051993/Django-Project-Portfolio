from django.db import models
from django.utils import timezone
# Create your models here.

class Contract(models.Model):
    contract_name = models.CharField(max_length=100,default='-')
    contract_type = models.CharField(max_length=100,default='-')
    contract_size = models.IntegerField(default=0)
    contract_startDate = models.DateField(default=timezone.now)
    contract_endDate = models.DateField(default=timezone.now)
    frequency = models.CharField(max_length = 100,default='0') 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    contract_priceType = models.CharField(max_length=100,default='-')

    
    
     
