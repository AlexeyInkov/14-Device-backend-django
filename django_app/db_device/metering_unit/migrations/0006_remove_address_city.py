# Generated by Django 5.0.7 on 2024-09-18 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metering_unit', '0005_address_latitude_address_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
    ]
