from django.shortcuts import render
from .forms import RegForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import Reg



def RegForm_Page(request):
    form = RegForm(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user = Reg(username=username,email=email,password=password)
        new_user.save()
    return render(request,'feedback.html',context)
