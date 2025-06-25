from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.forms import PasswordResetForm

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Enter password here'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter confirm here'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_confirm_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password missmatch")
        print(confirm_password)
        print(password)
        return confirm_password

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError('Username already taken')
        return username


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

