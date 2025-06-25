from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pid',
                  'pname',
                  'pcost',
                  'pcolor',
                  'pmfd',
                  'pexd']

class UpdateForm(forms.Form):
    pid = forms.CharField(label='Enter Pid', max_length=20)
    pcost = forms.CharField(label='Enter Pcost', max_length=10)

class DeleteForm(forms.Form):
    pid = forms.IntegerField()
