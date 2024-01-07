from .models import Deal
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['deal_label', 'deal_message', 'end_date', 'created_at', 'status', 'source', 'custom_field_1', 'custom_field_2']

        