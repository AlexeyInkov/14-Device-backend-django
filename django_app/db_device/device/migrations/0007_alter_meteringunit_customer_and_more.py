# Generated by Django 5.0.7 on 2024-08-12 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0006_alter_address_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meteringunit",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="metering_units_customer",
                to="device.organization",
            ),
        ),
        migrations.AlterField(
            model_name="meteringunit",
            name="service_organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="metering_units_service_organization",
                to="device.organization",
            ),
        ),
        migrations.AlterField(
            model_name="meteringunit",
            name="tso",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="metering_units_tso",
                to="device.tsorganization",
            ),
        ),
    ]
