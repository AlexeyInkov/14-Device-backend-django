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

from django.urls import path

from .views import message_view
from .views import (
    OrganizationListView,
    OrganizationCreateView,
    OrganizationDetailView,
    OrganizationUpdateView,
    OrganizationDeleteView,
    MeteringUnitCreateView,
    MeteringUnitDetailView,
    MeteringUnitListView,
    MeteringUnitUpdateView,
    MeteringUnitDeleteView,
)
from .views import MenuListAPIView, AddressListAPIView, DeviceListAPIView

app_name = "device"

urlpatterns = [
    path("menu/", MenuListAPIView.as_view(), name="menu"),
    path("addresses/", AddressListAPIView.as_view(), name="addresses"),
    path("devices/", DeviceListAPIView.as_view(), name="devices"),
    # path("msg_to_kafka/", message_view),
    # #
    # path("orgs/", OrganizationListView.as_view()),
    # path("org/", OrganizationCreateView.as_view()),
    # path("org/<int:pk>/", OrganizationDetailView.as_view()),
    # path("org/<int:pk>/update/", OrganizationUpdateView.as_view()),
    # path("org/<int:pk>/delete/", OrganizationDeleteView.as_view()),
    # #
    # path("meter-units/", MeteringUnitListView.as_view()),
    # path("meter-unit/", MeteringUnitCreateView.as_view()),
    # path("meter-unit/<int:pk>", MeteringUnitDetailView.as_view()),
    # path("meter-unit/<int:pk>/update", MeteringUnitUpdateView.as_view()),
    # path("meter-unit/<int:pk>/delete", MeteringUnitDeleteView.as_view()),
    # #
    # path("devices/", message_view),
    # path("device/", message_view),
    # path("device/<int:pk>", message_view),
    # path("device/<int:pk>/update", message_view),
    # path("device/<int:pk>/delete", message_view),
]
