# Generated by Django 5.0.1 on 2024-01-14 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0019_remove_deal_custom_field_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 14, 36, 53, 491349, tzinfo=datetime.timezone.utc)),
        ),
    ]
