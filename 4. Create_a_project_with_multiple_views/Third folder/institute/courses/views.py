from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def home(request):
    x='<h1 style="color:red">This is Durgasoft.</h1>'
    return HttpResponse(x)

def contact(request):
    c='<h1 style="color:Blue">Please goto main office to meet Dugra sir.</h1>'
    return HttpResponse(c)

def about(request):
    a='<h1 style="color:Green">We provide Multiple Skills here.</h1>'
    return HttpResponse(a)

def location(request):
    l='<h1 style="color:black">Durgasoft is located in Ameerpet.</h1>'
    return HttpResponse(l)
