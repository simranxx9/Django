# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# connector o connect database to app is pyscopg2
class Destination(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='Pictures')
    desc=models.TextField()
    price=models.IntegerField()
    offer = models.BooleanField(default=False)
