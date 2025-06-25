from django.shortcuts import render,HttpResponse
from .forms import ProductForm, UpdateForm, DeleteForm
from .models import Product
from django.template import loader


def home(request):
    return render(request,'home.html')

def insert(request):
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            data = "<h1>Insertion is successfully Done.</h1>" \
                    "<a href='./'> Goto Home</a>"
            return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form = ProductForm()
        return render(request,'insert.html',{'iform':form})

def details(request):
    det = Product.objects.all()
    if len(det)==0:
        data = "<h1> No Data Found </h1>" \
                    "<a href='./'> Goto Home</a>"
        return HttpResponse(data)
    else:
        template=loader.get_template('details.html')
        context={'det':det}
        r=template.render(context,request)
        return HttpResponse(r)

def update(request):
    if request.method=='POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['pid']
            id1 = int(id)
            cost=form.cleaned_data['pcost']
            cost1 = float(cost)
            dbuser=Product.objects.filter(pid=id1)
            if not dbuser:
                data="<h1>Invalid product Id.</h1>" \
                    "<a href='./'> Goto Home</a>"
                return HttpResponse(data)
            else:
                dbuser.update(pcost=cost1)
                data="<h1>Product Details update successfully.</h1>" \
                    "<a href='./'> Goto Home</a>"
                return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form=UpdateForm()
        return render(request,'update.html',{'uform':form})

def delete(request):
    if request.method=='POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            pid1=int(form.cleaned_data['pid'])
            dbuser=Product.objects.get(pid=pid1)
            if not dbuser:
                return HttpResponse('The given id is not available')
            else:
                dbuser.delete()
                data= "<h1>Delete successfully.</h1>" \
                    "<a href='./'> Goto Home</a>"
                return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form=DeleteForm()
        return render(request,'delete.html',{'dform':form})





