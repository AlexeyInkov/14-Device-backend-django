from django.urls import path, include
from rest_framework import routers


from .views import TypeToRegistryViewSet, DeviceVerificationViewSet

app_name = "device"

router = routers.DefaultRouter()
router.register(r"type_to_registry", TypeToRegistryViewSet, basename="type_to_registry")
router.register(
    r"device_verification", DeviceVerificationViewSet, basename="device_verification"
)

urlpatterns = [
    path("", include(router.urls)),
]
