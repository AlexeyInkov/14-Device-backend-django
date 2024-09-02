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
        fields = "id", "user", "organization"


class OrganizationSerializer(MySerializer):
    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
        )


class AddressSerializer(MySerializer):
    class Meta:
        model = Address
        fields = "__all__"


class MeteringUnitSerializer(MySerializer):
    class Meta:
        model = MeteringUnit
        fields = "__all__"
