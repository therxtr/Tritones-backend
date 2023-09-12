from django import forms
from .models import contactModel

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = contactModel
        exclude = []