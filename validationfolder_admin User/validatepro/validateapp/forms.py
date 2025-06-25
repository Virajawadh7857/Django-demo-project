from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class RegForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Pwd',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Confirm Password'
            }
        )
    )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("User name is taken already.")
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is taken already.")
        elif not 'gmail.com' in email:
            raise forms.ValidationError("Email has to end with gmail.com.")
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Pwd must be match.")
        elif len(password) <= 3 or len(password) >= 7:
            raise forms.ValidationError("pwd must be > 3 chars or <7.")
        return data
