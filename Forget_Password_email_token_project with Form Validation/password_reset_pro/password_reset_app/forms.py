from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

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

class PasswordReset_form(PasswordResetForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if not qs:
            raise forms.ValidationError('Invaild Email')
        return email


class SetPassword_form(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter password here'}))
    new_password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter confirm here'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password1')

    def clean_new_password2(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError("Password missmatch")
        print(new_password2)
        print(new_password1)
        return new_password2
