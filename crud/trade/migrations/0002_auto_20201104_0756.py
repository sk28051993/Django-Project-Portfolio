# Generated by Django 3.1.2 on 2020-11-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='trade_price',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='trade_quantity',
        ),
    ]