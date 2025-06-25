from django import forms

class ContactForm(forms.Form):
    fname = forms.CharField(label='First Name',
                            widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter your First Name'
                                }
                            )
                            )

    lname = forms.CharField(label='Last Name',
                            widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter your Last Name'
                                }
                            )
                            )

    username = forms.CharField(label='UserName',
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter your UserName'
                                   }
                               )
                               )

    Password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter your Password'
                                   }
                               )
                               )

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter your Email'
                                 }
                             )
                             )

    mobile = forms.IntegerField(label='Mobile no.',
                                widget=forms.NumberInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your Mobile no.'
                                    }
                                )
                                )



class LoginForm(forms.Form):
    username = forms.CharField(label='UserName',
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter your UserName'
                                   }
                               )
                               )

    Password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter your Password'
                                   }
                               )
                               )