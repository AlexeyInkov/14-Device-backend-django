from django.contrib.auth.models import User
from django.db import models


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
