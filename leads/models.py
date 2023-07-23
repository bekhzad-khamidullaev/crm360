from django.db import models
from products.models import Product


class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,  null=True)
    phoned = models.BooleanField(default=False)
    phoned_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.product}'