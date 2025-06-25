from .models import User,Teacher,Student
from django import forms

class Teacher_user(forms.ModelForm):
    password = forms.CharField(label='password')
    class Meta:
        model = User
        fields =['email', 'password']

class Teacher_profile(forms.ModelForm):
    class Meta:
        model= Teacher
        fields = ['name', 'age']


class Student_user(forms.ModelForm):
    password = forms.CharField(label='password')
    class Meta:
        model = User
        fields =['email', 'password']

class Student_profile(forms.ModelForm):
    class Meta:
        model= Student
        fields = ['name', 'phone', 'address']

class Teacher_loing_Form(forms.Form):
    email = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

class Student_loing_Form(forms.Form):
    email = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))







