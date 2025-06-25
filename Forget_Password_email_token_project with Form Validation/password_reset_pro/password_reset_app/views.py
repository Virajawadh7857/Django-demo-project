from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, PasswordReset_form, SetPassword_form

from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetView
from django.urls import reverse_lazy

class PasswordsResetView(PasswordResetView):
    form_class = PasswordReset_form
    #form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class PasswordsResetConfirmViews(PasswordResetConfirmView):
    form_class = SetPassword_form
    #form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')



def home(request):
    context={}
    return render(request, 'home.html', context)

def User_Registration(request):
    u_form = UserRegistrationForm(request.POST or None)
    if u_form.is_valid():
        new_user = u_form.save(commit=False)
        new_user.set_password(u_form.cleaned_data['password'])
        new_user.save()
        return redirect('home')
    context={
        'u_form':u_form,
    }
    return render(request, 'user_Registration.html',context)

def login_user(request):
    l_form = LoginForm(request.POST or None)
    if l_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('home')
    context = {
        'l_form': l_form,
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')


