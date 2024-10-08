# Generated by Django 5.0.7 on 2024-08-12 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0007_alter_meteringunit_customer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="devicemod",
            old_name="name",
            new_name="mod",
        ),
        migrations.RemoveField(
            model_name="devicetype",
            name="name",
        ),
        migrations.AddField(
            model_name="devicetype",
            name="registry_number",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="device.deviceregistrynumber",
            ),
        ),
    ]
