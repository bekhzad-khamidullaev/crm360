# Generated by Django 5.0.1 on 2024-01-14 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_remove_lead_company_remove_lead_contact_date_and_more'),
        ('organizations', '0003_company_state'),
        ('products', '0004_productcategory_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.company'),
        ),
        migrations.AddField(
            model_name='lead',
            name='contact_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='lead',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='lead',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products'),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.CharField(choices=[('phone', 'Phone'), ('social_network', 'Social Networks'), ('tv', 'Tv')], default='Phone', max_length=200),
        ),
        migrations.AddField(
            model_name='lead',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
