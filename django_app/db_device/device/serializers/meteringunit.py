from rest_framework import serializers

from ..models import (
    UserToOrganization,
    TSOrganization,
    Organization,
    Address,
    MeteringUnit,
)


class UserToOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToOrganization


class TSOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSOrganization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address


class MeteringUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeteringUnit
