# Generated by Django 5.0.7 on 2024-09-04 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0016_rename_device_id_deviceverification_device_and_more'),
        ('metering_unit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meteringunit',
            name='address',
        ),
        migrations.RemoveField(
            model_name='meteringunit',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='meteringunit',
            name='service_organization',
        ),
        migrations.RemoveField(
            model_name='meteringunit',
            name='tso',
        ),
        migrations.AlterField(
            model_name='device',
            name='metering_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='device', to='metering_unit.meteringunit'),
        ),
        migrations.RemoveField(
            model_name='usertoorganization',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='usertoorganization',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='MeteringUnit',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='UserToOrganization',
        ),
    ]
