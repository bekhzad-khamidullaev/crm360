# Generated by Django 5.0.1 on 2024-01-14 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0007_alter_deal_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 13, 1, 20, 621920, tzinfo=datetime.timezone.utc)),
        ),
    ]
