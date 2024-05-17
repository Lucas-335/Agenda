from django import forms
from contact.models import Contact
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','last_name','number','email','category', 'image']

        error_messages = {
            'number':{
                'invalid':'Informe um número de telefone válido',
            }
        }

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Primeiro Nome',required=True)
    last_name = forms.CharField(label='Segundo Nome',required=True)
    email = forms.EmailField(label='Email',required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

    def clean_email(self):
        data_email = self.cleaned_data.get('email')
        if User.objects.filter(**{'email':data_email}).exists():
            self.add_error('email',ValidationError('Email já utilizado',code='invalid'))
        return data_email
    
class LoginForm(AuthenticationForm):
    ...