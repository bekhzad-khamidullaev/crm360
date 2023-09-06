from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Products(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    count = models.PositiveBigIntegerField(null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.count}'

    class Meta:
        ordering = ['name']
=======
class Product(models.Model):
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product_id} {self.product_name}'
>>>>>>> e039bc4e4e6d77f5b95067663c9e0c973901d6bc
