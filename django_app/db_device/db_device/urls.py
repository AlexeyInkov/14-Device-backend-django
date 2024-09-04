from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import settings

schema_view = get_schema_view(
    openapi.Info(
        title="myproject",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path(
            "api/docs/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path("auth/", include("my_auth.urls")),
        path("api/metering_unit/", include("metering_unit.urls")),
        path("api/device/", include("device.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
