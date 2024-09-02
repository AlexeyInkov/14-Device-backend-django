from rest_framework import serializers

from .address import MeteringUnitSerializer
from .baseserializers import MySerializer
from ..models import (
    DeviceInstallationPoint,
    DeviceRegistryNumber,
    DeviceType,
    DeviceMod,
    Device,
    DeviceVerification,
    TypeToRegistry,
)


class DeviceInstallationPointSerializer(MySerializer):
    class Meta:
        model = DeviceInstallationPoint
        fields = "id", "name"


class DeviceRegistryNumberSerializer(MySerializer):
    class Meta:
        model = DeviceRegistryNumber
        fields = "id", "registry_number"


class DeviceTypeSerializer(MySerializer):
    class Meta:
        model = DeviceType
        fields = "id", "type"


class DeviceModSerializer(MySerializer):
    class Meta:
        model = DeviceMod
        fields = "id", "mod"


class TypeToRegistrySerializer(MySerializer):
    numbers_registry = serializers.CharField(required=False)

    class Meta:
        model = TypeToRegistry
        fields = "id", "device_type_file", "numbers_registry"


class DeviceSerializer(MySerializer):
    metering_unit = MeteringUnitSerializer()
    installation_point = DeviceInstallationPointSerializer()
    registry_number = DeviceRegistryNumberSerializer(required=False)
    type = DeviceTypeSerializer(required=False)
    mod = DeviceModSerializer(required=False)
    type_to_fields = TypeToRegistrySerializer()
    nodes = serializers.CharField(required=False)

    class Meta:
        model = Device
        fields = (
            "id",
            "metering_unit",
            "installation_point",
            "registry_number",
            "type",
            "mod",
            "type_to_file",
            "factory_number",
            "nodes",
        )


class DeviceVerificationSerializer(MySerializer):
    # device = DeviceSerializer()
    organization = serializers.CharField(required=False)
    verification_date = serializers.DateField(required=False)

    class Meta:
        model = DeviceVerification
        fields = (
            "id",
            "device",
            "organization",
            "verification_date",
            "valid_date",
            "is_actual",
        )
