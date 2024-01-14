from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from organizations.models import Company
from contacts.models import Contacts
from users.models import Users


class Deal(models.Model):

    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(default=timezone.timedelta(days=10))
    
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        WON = 'won', 'Won'
        LOST = 'lost', 'Lost'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN,
    )

    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    probability = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    deal_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    closing_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:50]

