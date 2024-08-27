from rest_framework import serializers

from django_app.db_device.device.models import (
    DeviceInstallationPoint,
    DeviceRegistryNumber,
    DeviceType,
    DeviceMod,
    Device,
    DeviceVerification,
    TypeToRegistry,
)


class DeviceInstallationPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInstallationPoint


class DeviceRegistryNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceRegistryNumber


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType


class DeviceModSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceMod


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device


class DeviceVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceVerification


class TypeToRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeToRegistry
