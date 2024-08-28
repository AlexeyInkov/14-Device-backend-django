from django.contrib import admin

from .models import (
    UserToOrganization,
    Organization,
    Address,
    MeteringUnit,
    DeviceInstallationPoint,
    DeviceRegistryNumber,
    DeviceType,
    DeviceMod,
    Device,
    DeviceVerification,
    TypeToRegistry,
)


admin.site.register(UserToOrganization)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(MeteringUnit)
admin.site.register(DeviceInstallationPoint)
admin.site.register(DeviceRegistryNumber)
admin.site.register(DeviceType)
admin.site.register(DeviceMod)
admin.site.register(Device)
admin.site.register(DeviceVerification)
admin.site.register(TypeToRegistry)
