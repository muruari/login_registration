# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    return redirect('/users')

def users(request):
    context = {'users': Users.objects.all()}
    return render(request,'users.html', context)

def create_user(request):
    errors = Users.objects.validator(request.POST) #connects this to class Users/models.py
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        Users.objects.create(full_name=request.POST['FN']+" "+request.POST['LN'], email=request.POST['email'])
        return redirect('/users')

def show(request, id):
    context = {'users': Users.objects.get(id=id)}
    return render(request, 'show.html', context)

def new(request):
    return render(request, 'new.html')

def process_edit(request, id):
    errors = Users.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+id)
    else:
#    email=request.post['EML']
        user=Users.objects.get(id=id)
        print user.full_name
        f = request.POST['FN']
        l = request.POST['LN']
        e = request.POST['EML']
        user.full_name = f +" "+ l
        user.email = e
        user.save()
        return redirect('/restful_users/show/'+id)
    
def edit(request, id):
    context = {
        'user': Users.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def destroy(request, id):
    d = Users.objects.get(id=id)
    d.delete()
    return redirect('/')