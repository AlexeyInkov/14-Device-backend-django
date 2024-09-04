from django.urls import path, include
from rest_framework import routers

from .views import (
    MeteringUnitViewSet,
    AddressViewSet,
    OrganizationViewSet,
    UserToOrganizationViewSet,
)

app_name = "metering_unit"

router = routers.DefaultRouter()
router.register(r"m_unit", MeteringUnitViewSet, basename="m_unit")
router.register(r"organization", OrganizationViewSet, basename="organization")
router.register(
    r"user_to_organization", UserToOrganizationViewSet, basename="user_to_organization"
)
router.register(r"address", AddressViewSet, basename="address")

urlpatterns = [
    path("", include(router.urls)),
]
