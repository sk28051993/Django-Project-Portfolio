# Generated by Django 3.1.2 on 2020-11-04 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_trade_trade_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='eemail',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='ename',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='name',
        ),
    ]