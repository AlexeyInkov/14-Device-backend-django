from .baseserializers import MySerializer
from .models import (
    UserToOrganization,
    Organization,
    Address,
    MeteringUnit,
    Street,
    TypeStreet,
    Region,
)


class UserToOrganizationSerializer(MySerializer):
    class Meta:
        model = UserToOrganization
        fields = "id", "user", "organization"


class OrganizationSerializer(MySerializer):
    class Meta:
        model = Organization
        fields = "id", "name"


class RegionSerializer(MySerializer):
    class Meta:
        model = Region
        fields = "id", "name"


class TypeStreetSerializer(MySerializer):
    class Meta:
        model = TypeStreet
        fields = "id", "name"


class StreetSerializer(MySerializer):
    class Meta:
        model = Street
        fields = "id", "name"


class AddressSerializer(MySerializer):
    class Meta:
        model = Address
        fields = "__all__"


class MeteringUnitSerializer(MySerializer):
    class Meta:
        model = MeteringUnit
        fields = "__all__"
