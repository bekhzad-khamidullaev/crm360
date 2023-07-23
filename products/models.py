from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=100)
