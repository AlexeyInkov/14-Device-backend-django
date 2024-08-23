from rest_framework import serializers

from .models import (
    MeteringUnit,
    TSOrganization,
    Device,
    DeviceVerification,
)


class CustomerSerializer(serializers.Serializer):
    id = serializers.CharField(source="customer__id", read_only=True)
    name = serializers.CharField(source="customer__name", read_only=True)

    class Meta:
        model = MeteringUnit
        fields = (
            "id",
            "name",
        )


class MenuSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    def get_customers(self, obj):
        qs = (
            MeteringUnit.objects.filter(tso=obj.id)
            .values("customer__id", "customer__name")
            .distinct()
        )
        serializer = CustomerSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = TSOrganization
        fields = (
            "id",
            "name",
            "customers",
        )


class AddressSerializer(serializers.ModelSerializer):
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
    ITP = serializers.CharField(source="address.ITP", read_only=True)

    class Meta:
        model = MeteringUnit
        fields = (
            "customer",
            "service_organization",
            "tso",
            "city",
            "street",
            "house_number",
            "corp",
            "liter",
            "ITP",
        )


class DeviceVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceVerification
        fields = (
            "verification_date",
            "valid_date",
        )


class DeviceSerializer(serializers.ModelSerializer):
    installation_point = serializers.CharField(
        source="installation_point.name", read_only=True
    )
    registry_number = serializers.CharField(
        source="registry_number.registry_number", read_only=True
    )
    device_type = serializers.CharField(source="device_type.type", read_only=True)
    device_mod = serializers.CharField(source="device_mod.mod", read_only=True)
    factory_number = serializers.CharField(read_only=True)
    verification = DeviceVerificationSerializer(
        source="filtered_verifications",
        many=True,
        read_only=True,
    )

    class Meta:
        model = Device
        fields = (
            "installation_point",
            "registry_number",
            "device_type",
            "device_mod",
            "factory_number",
            "verification",
        )
