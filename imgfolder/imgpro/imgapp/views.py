from django.shortcuts import render
from imgapp import forms
from imgapp.forms import LoginForm


def index(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            return render(request,'output.html')
        else:
            print(forms.errors)
    else:
        form = LoginForm()
        return render(request,'display.html',{'form3':form})






#create static folder in imgpro.
#create images folder in static folder.
#note: copy any image from our drive and paste images folder.
#create html file with name 'display.html' in templates folder.