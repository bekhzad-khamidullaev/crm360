# Generated by Django 5.0.1 on 2024-01-14 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_alter_lead_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='company',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='phoned',
        ),
    ]
