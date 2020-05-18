# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'INVALID CREDENTIAL')
            return redirect('accounts:register')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            if User.objects.filter(username=u).exists():
                messages.info(request,"USERNAME EXISTS")
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username = u,password= p1,email= e,first_name=f,last_name=l)
                user.save();
                return redirect('/')
        else:
            messages.info(request,"PASSWORD INCORRECT")
            return redirect('accounts:register')
    else: 
        return render(request,'register.html')