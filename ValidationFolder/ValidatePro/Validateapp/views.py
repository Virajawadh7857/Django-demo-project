from django.shortcuts import render
from .forms import RegForm
from .models import Reg
from django.contrib.auth.hashers import make_password



def RegForm_Page(request):
    form = RegForm(request.POST or None)
    context ={
        'form' : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        hashed_password=make_password(password)
        new_user = Reg(username=username,email=email,password=hashed_password)
        new_user.save()
        print(new_user)
    return render(request,'feedback.html',context)
