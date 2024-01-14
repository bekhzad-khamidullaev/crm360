# Generated by Django 5.0.1 on 2024-01-14 14:35

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_contact_company_alter_contacts_options_and_more'),
        ('deals', '0018_alter_deal_end_date'),
        ('organizations', '0003_company_state'),
        ('users', '0002_rename_company_jobt_rename_contact_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='custom_field_1',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='custom_field_2',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='deal_label',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='deal_message',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='source',
        ),
        migrations.AddField(
            model_name='deal',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
        migrations.AddField(
            model_name='deal',
            name='closing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.company'),
        ),
        migrations.AddField(
            model_name='deal',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contacts'),
        ),
        migrations.AddField(
            model_name='deal',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 14, 35, 41, 677847, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='deal',
            name='deal_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='deal',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='probability',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='deal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
