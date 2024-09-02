from django.urls import path, include
from rest_framework import routers

from .views import (
    MenuListAPIView,
    AddressListAPIView,
    DeviceListAPIView,
    OrganizationListAPIView,
)
from .views import TypeToRegistryViewSet, DeviceVerificationViewSet

app_name = "device"

router = routers.DefaultRouter()
router.register(r"type_to_registry", TypeToRegistryViewSet, basename="type_to_registry")
router.register(
    r"device_verification", DeviceVerificationViewSet, basename="device_verification"
)

urlpatterns = [
    path("menu/", MenuListAPIView.as_view(), name="menu"),
    path("addresses/", AddressListAPIView.as_view(), name="addresses"),
    path("devices/", DeviceListAPIView.as_view(), name="devices"),
    path("organizations/", OrganizationListAPIView.as_view(), name="organizations"),
    path("", include(router.urls)),
]
