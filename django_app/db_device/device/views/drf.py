from tkinter import Menu

from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from ..models import (
    MeteringUnit,
    Device,
    DeviceVerification,
    Organization,
    UserToOrganization,
)
from ..serializers import (
    MenuSerializer,
    AddressesSerializer,
    ShortDeviceSerializer,
    UserToOrganizationSerializer,
)


class MenuListAPIView(ListAPIView):
    queryset = Organization.objects.prefetch_related("mu_tso").filter(
        pk__in=MeteringUnit.objects.values_list("tso", flat=True)
    )
    serializer_class = MenuSerializer


class AddressListAPIView(ListAPIView):
    serializer_class = AddressesSerializer

    def get_queryset(self):
        queryset = (
            MeteringUnit.objects.select_related("customer")
            .select_related("service_organization")
            .select_related("tso")
            .select_related("address")
        )
        if self.request.query_params.get("customer") is None:
            return queryset
        return queryset.filter(customer=self.request.query_params.get("customer"))


class DeviceListAPIView(ListAPIView):
    serializer_class = ShortDeviceSerializer

    def get_queryset(self):
        queryset = (
            Device.objects
            # .select_related("registry_number__device_type_set")
            .select_related("type_of_file")
            .select_related("mod")
            .select_related("installation_point")
            .select_related("metering_unit")
            .prefetch_related(  # "verifications")
                Prefetch(
                    "verifications",
                    queryset=DeviceVerification.objects.filter(
                        is_actual=True, is_delete=False
                    ),
                )
            )
            # .filter(verifications__is_actual=True)
        )
        if self.request.query_params.get("metering_unit") is None:
            return queryset
        return queryset.filter(
            metering_unit=self.request.query_params.get("metering_unit")
        )


class OrganizationListAPIView(ListAPIView):
    serializer_class = UserToOrganizationSerializer

    def get_queryset(self):
        return User.objects.prefetch_related("user_to_org__organization").filter(
            user=self.request.user
        )
