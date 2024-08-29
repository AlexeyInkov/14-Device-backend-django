"""
URL configuration for db_device project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers

from .views import MenuListAPIView, AddressListAPIView, DeviceListAPIView
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
    path("", include(router.urls)),
]
