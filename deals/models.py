from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator


class Deal(models.Model):
    deal_label = models.CharField(max_length=100, blank=True, null=True)
    deal_message = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=10))
    
    # Deal status choices
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    
    # Related fields
    # contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # Deal source (e.g., where the lead came from)
    source = models.CharField(max_length=255, blank=True, null=True)
    
    # Assigned user (salesperson responsible for the deal)
    # assigned_to = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    
    # Probability of closing the deal (as a percentage)
    # probability = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    
    # Custom fields (you can add more as needed)
    custom_field_1 = models.CharField(max_length=255, blank=True, null=True)
    custom_field_2 = models.CharField(max_length=255, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.deal_label