# Generated by Django 3.1.2 on 2020-11-04 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_contract_contract_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_endDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_startDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
