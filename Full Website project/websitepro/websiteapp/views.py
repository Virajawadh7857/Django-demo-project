from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm
from .models import Student

def home_page(request):
    context={
        'name': 'Narayana',
        'content':'Welcome to home page'
    }
    return render(request,'home.html')

def contact_page(request):
    '''context={
        'name': 'Narayana',
        'content': 'Contact Us Form'
    }'''
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contacts.html',{'cform':contact_form})

def about_page(request):
    return render(request,'about.html')

def services_page(request):
    return render(request,'services.html')

def register_page(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = request.POST.get('fname', '')
            lname = request.POST.get('lname', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
        person = Student(fname=fname, lname=lname, username=username,
                         password=password,email=email,mobile=mobile)
        person.save()
        return redirect('/#/')
    else:
        form = ContactForm()
        return render(request,'myregister.html',{'rform':form})

def login_page(request):
    if request.method=="POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username2 = request.POST.get('username', '')
            password2 = request.POST.get('password', '')
            dbuser = Student.objects.filter(username=username2, password=password2)
            if dbuser:
                return redirect('/home/')
            else:
                return redirect('/#/')
    else:
        login_form = LoginForm()
        return render(request,'login.html',{'login_form':login_form})



