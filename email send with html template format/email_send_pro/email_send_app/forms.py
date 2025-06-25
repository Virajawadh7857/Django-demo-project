from django import forms


class Contact_Form(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    mobile_no = forms.CharField(required=True, max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No.'}))
    message = forms.CharField(required=True, max_length=200, help_text='required 200 words only', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Messages.'}))