from pydoc import describe
from signal import signal
from unicodedata import name
from django.db import models
import random

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4,default="null")
    description = models.TextField(null=True, blank=True)
    currency = models.ForeignKey('Currency', null=True, on_delete=models.SET_NULL)
    def get_random_price(self):
        return random.randint(0,2500)
        
class Currency(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4)
    sign = models.CharField(max_length=1)
    def __str__(self):
        return self.sign