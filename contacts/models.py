from django.db import models
from leads.models import Lead
from products.models import Product

class Contacts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.ForeignKey(Lead, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)