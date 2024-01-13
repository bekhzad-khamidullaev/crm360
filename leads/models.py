from django.db import models
from products.models import Products


class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,  null=True)
    phoned = models.BooleanField(default=False)
    # phoned_at = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        ('phone', 'Phone'),
        ('social_network', 'Social Networks'),
        ('tv', 'Tv'),
    )
    source = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Phone')
    email = models.EmailField(max_length=254, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    contact_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.product}'
    
