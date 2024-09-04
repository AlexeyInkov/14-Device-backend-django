from django.contrib import admin

from .models import (
    UserToOrganization,
    Organization,
    Address,
    MeteringUnit,
)

admin.site.register(UserToOrganization)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(MeteringUnit)
