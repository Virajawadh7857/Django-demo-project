from django import forms
from django.contrib.auth.models import User


class userform (forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder':'Enter Username'}),required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
        'placeholder':'Enter Email'}),required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Enter your first name'}), required=False, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Enter your last name'}), required=False,max_length=50)
    password = forms.CharField( help_text="Password must have 1 Alphabate, 1 number and 1 special charatcher",widget=forms.PasswordInput(attrs={'class':'form-control',
        'placeholder':'Enter password'}),required=True,max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Confirm password' }), required=True,max_length=50,)

    class Meta():
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username hai Db me")
        return username

    def clean_confirm_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password missmatch")
        print(confirm_password)
        print(password)
        return confirm_password

