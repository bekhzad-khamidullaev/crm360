# Generated by Django 4.1.3 on 2023-09-26 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0002_alter_deal_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="end_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 10, 6, 14, 51, 2, 75864, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]