from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(BaseTimeModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "organizations"


class MeteringUnit(BaseTimeModel):

    customer = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name="metering_units_customer",
    )
    service_organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name="metering_units_service_organization",
    )
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "metering_units"


class DeviceRegistryNumber(BaseTimeModel):

    registry_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "device_registry_numbers"


class DeviceType(BaseTimeModel):

    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "device_types"


class DeviceMod(BaseTimeModel):

    name = models.CharField(max_length=100)
    type_devise = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "device_mods"


class DeviceInstallationPoint(BaseTimeModel):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "device_installation_points"


class Device(BaseTimeModel):

    registry_number = models.ForeignKey(
        DeviceRegistryNumber, on_delete=models.SET_NULL, null=True
    )
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    device_mod = models.ForeignKey(DeviceMod, on_delete=models.SET_NULL, null=True)
    factory_number = models.CharField(max_length=100)
    installation_point = models.ForeignKey(
        DeviceInstallationPoint, on_delete=models.SET_NULL, null=True
    )
    notes = models.CharField(max_length=100)
    metering_unit = models.ForeignKey(
        MeteringUnit, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = "devices"


class DeviceVerification(BaseTimeModel):

    device_id = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    organization = models.CharField(max_length=100)
    verification_date = models.DateField(default="1900-01-01")
    valid_date = models.DateField(default="1900-01-01")

    class Meta:
        verbose_name_plural = "device_verifications"
