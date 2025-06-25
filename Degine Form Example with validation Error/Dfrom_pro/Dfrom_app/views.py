from django.shortcuts import render
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                     email=email, password=password)
            messages.success(request,('user registration successfully'))
            return HttpResponseRedirect('/')
    else :
        form = userform()
    return render(request,'registration.html',{'frm':form})