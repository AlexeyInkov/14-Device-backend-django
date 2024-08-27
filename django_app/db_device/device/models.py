from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TSOrganization(BaseTimeModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "ts_organizations"

    def __str__(self):
        return self.name


class Organization(BaseTimeModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "organizations"

    def __str__(self):
        return self.name


class UserToOrganization(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    actual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "users_to_organizations"

    def __str__(self):
        return f"{self.user.username} ({self.organization.name})"


class Address(BaseTimeModel):
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    house_number = models.CharField(max_length=100, null=True, blank=True)
    corp = models.CharField(max_length=100, null=True, blank=True)
    liter = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        return ",".join(
            map(
                str,
                (
                    self.city,
                    self.street,
                    self.house_number,
                    self.corp,
                    self.liter,
                ),
            )
        )


class MeteringUnit(BaseTimeModel):

    customer = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="metering_units_customer",
    )
    service_organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="metering_units_service_organization",
    )
    tso = models.ForeignKey(
        TSOrganization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="metering_units_tso",
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        related_name="metering_units_address",
    )
    ITP = models.CharField(max_length=10, null=True, blank=True)
    totem_number = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "metering_units"

    def __str__(self):
        return f"{self.address} {self.ITP}"


class DeviceRegistryNumber(BaseTimeModel):

    registry_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "device_registry_numbers"

    def __str__(self):
        return str(self.registry_number)


class DeviceType(BaseTimeModel):

    type = models.CharField(max_length=100)
    registry_number = models.ForeignKey(
        DeviceRegistryNumber, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = "device_types"

    def __str__(self):
        return self.type


class DeviceMod(BaseTimeModel):

    mod = models.CharField(max_length=100)
    # type_devise = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "device_mods"

    def __str__(self):
        return self.mod


class DeviceInstallationPoint(BaseTimeModel):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "device_installation_points"

    def __str__(self):
        return self.name


class Device(BaseTimeModel):
    metering_unit = models.ForeignKey(
        MeteringUnit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    installation_point = models.ForeignKey(
        DeviceInstallationPoint,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    registry_number = models.ForeignKey(
        DeviceRegistryNumber,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    device_type = models.ForeignKey(
        DeviceType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    device_mod = models.ForeignKey(
        DeviceMod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    factory_number = models.CharField(max_length=100)

    notes = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "devices"

    def __str__(self):
        return f"{str(self.device_mod)} №{self.factory_number}"


class DeviceVerification(BaseTimeModel):

    device_id = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, related_name="verifications"
    )
    organization = models.CharField(max_length=100, blank=True, null=True)
    verification_date = models.DateField(default="1900-01-01")
    valid_date = models.DateField(default="1900-01-01")
    is_actual = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "device_verifications"

    def __str__(self):
        return f"{self.verification_date}"
