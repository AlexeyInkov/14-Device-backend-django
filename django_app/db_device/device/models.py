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

    class Meta:
        verbose_name_plural = "organizations"

    def __str__(self):
        return self.name


class UserToOrganization(BaseTimeModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_to_org",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_to_org",
    )
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
        related_name="mu_c",
    )
    service_organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mu_so",
    )
    tso = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name="mu_tso",
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        related_name="mu_address",
    )
    itp = models.CharField(max_length=10, null=True, blank=True)
    totem_number = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "metering_units"

    def __str__(self):
        return f"{self.address} {self.itp}"


class DeviceRegistryNumber(BaseTimeModel):

    registry_number = models.CharField(unique=True, max_length=10)

    class Meta:
        verbose_name_plural = "device_registry_numbers"

    def __str__(self):
        return str(self.registry_number)


class DeviceType(BaseTimeModel):

    type = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "device_types"

    def __str__(self):
        return self.type


class DeviceMod(BaseTimeModel):

    mod = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "device_mods"

    def __str__(self):
        return self.mod


class DeviceInstallationPoint(BaseTimeModel):

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "device_installation_points"

    def __str__(self):
        return self.name


class TypeToRegistry(BaseTimeModel):
    device_type_file = models.CharField(max_length=100, unique=True)
    numbers_registry = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "types_to_registry"

    def __str__(self):
        return f"{self.device_type_file} - ({self.numbers_registry})"


class Device(BaseTimeModel):
    metering_unit = models.ForeignKey(
        MeteringUnit,
        on_delete=models.SET_NULL,
        null=True,
        related_name="device",
    )
    installation_point = models.ForeignKey(
        DeviceInstallationPoint,
        on_delete=models.SET_NULL,
        null=True,
        related_name="device",
    )
    registry_number = models.ForeignKey(
        DeviceRegistryNumber,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="device",
    )
    type = models.ForeignKey(
        DeviceType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="device",
    )
    mod = models.ForeignKey(
        DeviceMod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="device",
    )
    type_of_file = models.ForeignKey(
        TypeToRegistry,
        on_delete=models.SET_NULL,
        null=True,
        related_name="device",
    )
    factory_number = models.CharField(max_length=100, unique=True)

    notes = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "devices"

    def __str__(self):
        return f"{str(self.mod)} №{self.factory_number}"


class DeviceVerification(BaseTimeModel):

    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        null=True,
        related_name="verifications",
    )
    organization = models.CharField(max_length=100, blank=True, null=True)
    verification_date = models.DateField()
    valid_date = models.DateField(default="1900-01-01")
    is_actual = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "device_verifications"

    def __str__(self):
        return f"{self.verification_date}"
