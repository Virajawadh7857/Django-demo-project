from django import forms

class LoginForm(forms.Form):
    username = forms.CharField( label='User Name',
                                widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter Your User Name'
                                    }
                                )
                            )

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter Your Password'
                                   }
                               )
                            )