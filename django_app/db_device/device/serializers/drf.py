from django.contrib.auth.models import User
from rest_framework import serializers

from .address import OrganizationSerializer
from .baseserializers import MySerializer
from ..models import (
    MeteringUnit,
    Organization,
    Device,
    DeviceVerification,
)


class MenuCustomerSerializer(MySerializer):
    id = serializers.CharField(source="customer__id", read_only=True)
    name = serializers.CharField(source="customer__name", read_only=True)

    class Meta:
        model = MeteringUnit
        fields = (
            "id",
            "name",
        )


class MenuSerializer(MySerializer):
    customers = serializers.SerializerMethodField()

    def get_customers(self, obj):
        qs = (
            MeteringUnit.objects.filter(tso=obj.id)
            .values("customer__id", "customer__name")
            .distinct()
        )
        serializer = MenuCustomerSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "customers",
        )


class AddressesSerializer(MySerializer):
    customer = serializers.CharField(source="customer.name", read_only=True)
    service_organization = serializers.CharField(
        source="service_organization.name", read_only=True
    )
    tso = serializers.CharField(source="tso.name", read_only=True)
    city = serializers.CharField(source="address.city", read_only=True)
    street = serializers.CharField(source="address.street", read_only=True)
    house_number = serializers.CharField(source="address.house_number", read_only=True)
    corp = serializers.CharField(source="address.corp", read_only=True)
    liter = serializers.CharField(source="address.liter", read_only=True)
    itp = serializers.CharField(read_only=True)

    class Meta:
        model = MeteringUnit
        fields = (
            "id",
            "customer",
            "service_organization",
            "tso",
            "city",
            "street",
            "house_number",
            "corp",
            "liter",
            "itp",
        )


class ShortDeviceVerificationSerializer(MySerializer):
    class Meta:
        model = DeviceVerification
        fields = (
            "id",
            "valid_date",
        )


class ShortDeviceSerializer(MySerializer):
    installation_point = serializers.CharField(
        source="installation_point.name", read_only=True
    )

    type_of_file = serializers.CharField(
        source="type_of_file.device_type_file", read_only=True
    )

    factory_number = serializers.CharField(read_only=True)
    verification = ShortDeviceVerificationSerializer(
        source="filtered_verifications",
        many=True,
        read_only=True,
    )
    nodes = serializers.CharField(read_only=True)

    class Meta:
        model = Device
        fields = (
            "id",
            "installation_point",
            "type_of_file",
            "factory_number",
            "verification",
            "nodes",
        )


class UserOrganizationSerializer(MySerializer):
    organizations = serializers.SerializerMethodField()

    def get_organizations(self, obj):
        qs = Organization.objects.filter(user_to_org__user=obj.id).values("id", "name")
        serializer = OrganizationSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "organizations",
        )
