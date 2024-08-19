# Generated by Django 5.0.7 on 2024-08-12 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0008_rename_name_devicemod_mod_remove_devicetype_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="device_mod",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.devicemod",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="device_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="installation_point",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.deviceinstallationpoint",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="metering_unit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.meteringunit",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="notes",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="device",
            name="registry_number",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.deviceregistrynumber",
            ),
        ),
    ]
