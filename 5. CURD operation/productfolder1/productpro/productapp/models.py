from __future__ import unicode_literals
from django.db import models
import datetime as dt

mdate = dt.datetime.now()
dur = dt.datetime.now()+dt.timedelta(days=730)

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=20)
    pcost = models.DecimalField(max_digits=15, decimal_places=2)
    pcolor = models.CharField(max_length=20,default='black')
    pmfd = models.DateTimeField(default= mdate)
    pexd = models.DateTimeField(default= dur)
