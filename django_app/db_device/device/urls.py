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

app_name = "device"

urlpatterns = [
    path("msg_to_kafka/", message_view),
    #
    path("orgs/", message_view),
    path("org/", message_view),
    path("org/<pk:int>", message_view),
    path("org/<pk:int>/update", message_view),
    path("org/<pk:int>/delete", message_view),
    #
    path("meter-units/", message_view),
    path("meter-unit/", message_view),
    path("meter-unit/<pk:int>", message_view),
    path("meter-unit/<pk:int>/update", message_view),
    path("meter-unit/<pk:int>/delete", message_view),
    #
    path("devices/", message_view),
    path("device/", message_view),
    path("device/<pk:int>", message_view),
    path("device/<pk:int>/update", message_view),
    path("device/<pk:int>/delete", message_view),
]
