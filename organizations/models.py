from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    industry = models.CharField(max_length=100, blank=True, null=True, verbose_name="Industry")
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="State")
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name="Region")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Postal Code")
    country = models.CharField(max_length=100, default="Uzbekistan", verbose_name="Country")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Companies"
