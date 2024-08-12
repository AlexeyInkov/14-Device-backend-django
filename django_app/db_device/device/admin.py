from django.contrib import admin

from .models import (
    TSOrganization,
    Organization,
    Address,
    MeteringUnit,
    Device,
    DeviceVerification,
)

admin.site.register(TSOrganization)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(MeteringUnit)
admin.site.register(Device)
admin.site.register(DeviceVerification)
