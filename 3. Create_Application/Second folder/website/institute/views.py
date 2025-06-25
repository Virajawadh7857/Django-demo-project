from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    x='<h1 style="color:red">Welcome to Django World.</h1>'
    return HttpResponse(x)