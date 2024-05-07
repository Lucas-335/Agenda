from django import forms
from contact.models import Contact
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','last_name','number','email','category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-field'}),
            'last_name': forms.TextInput(attrs={'class':'input-field'}),
            'number': forms.TextInput(attrs={'class':'input-field'}),
            'email': forms.TextInput(attrs={'class':'input-field'}),            
            'category':forms.Select(attrs={'class':'input-field'})
        }
        error_messages = {
            'number':{
                'invalid':'Informe um número de telefone válido',
            }
        }
