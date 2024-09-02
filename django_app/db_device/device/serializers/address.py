from .baseserializers import MySerializer
from ..models import (
    UserToOrganization,
    Organization,
    Address,
    MeteringUnit,
)


class UserToOrganizationSerializer(MySerializer):
    class Meta:
        model = UserToOrganization


class OrganizationSerializer(MySerializer):
    class Meta:
        model = Organization


class AddressSerializer(MySerializer):
    class Meta:
        model = Address


class MeteringUnitSerializer(MySerializer):
    class Meta:
        model = MeteringUnit
