from django.db import models
from products.models import Products
from organizations.models import Company


class Lead(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,  null=True)
    SOURCE_CHOICES = (
        ('phone', 'Phone'),
        ('social_network', 'Social Networks'),
        ('tv', 'Tv'),
    )
    source = models.CharField(max_length=200, choices=SOURCE_CHOICES, default='Phone')
    email = models.EmailField(max_length=254, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, default=None)
    contact_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.product}'
    
