# Generated by Django 5.0.1 on 2024-01-14 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_alter_lead_company'),
        ('organizations', '0003_company_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.company'),
        ),
    ]
