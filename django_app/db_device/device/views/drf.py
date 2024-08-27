from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from ..models import (
    TSOrganization,
    MeteringUnit,
    Device,
    DeviceVerification,
)
from ..serializers import MenuSerializer, AddressSerializer, DeviceSerializer


class MenuListAPIView(ListAPIView):
    queryset = TSOrganization.objects.prefetch_related("metering_units_tso")
    #     Prefetch(
    #         ,
    #         queryset=MeteringUnit.objects.all(),
    #         to_attr="filtered_metering_units_tso",
    #     )
    # )
    serializer_class = MenuSerializer


class AddressListAPIView(ListAPIView):
    serializer_class = AddressSerializer

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
    serializer_class = DeviceSerializer

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
                    queryset=DeviceVerification.objects.filter(is_actual=True),
                    to_attr="filtered_verifications",
                )
            )
            # .filter(verifications__is_actual=True)
        )
        if self.request.query_params.get("metering_unit") is None:
            return queryset
        return queryset.filter(
            metering_unit=self.request.query_params.get("metering_unit")
        )
