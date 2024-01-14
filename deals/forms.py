from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from .models import Deal
from contacts.models import Contacts
from organizations.models import Company
from users.models import Users
class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        exclude = ['created_at', 'updated_at', 'deadline']

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), required=False)
    status = forms.ChoiceField(choices=Deal.Status.choices, initial=Deal.Status.OPEN)
    deadline = forms.DateField(initial=timezone.now() + timezone.timedelta(days=10))
    contact = forms.ModelChoiceField(queryset=Contacts.objects.all(), required=False)
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    assigned_to = forms.ModelChoiceField(queryset=Users.objects.all(), required=False)
    probability = forms.IntegerField(initial=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    deal_value = forms.DecimalField(initial=0.0, max_digits=10, decimal_places=2)
    closing_date = forms.DateField(required=False)

