from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        contacts = '__all__'
        exclude = ['created_at', 'updated_at', 'deadline']