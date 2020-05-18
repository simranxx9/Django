# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Destination

def index(request):
    dests = Destination.objects.all()      #to fetch the values from the database
    return render(request,'index.html',{'dests':dests})

# Create your views here.
