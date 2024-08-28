from rest_framework.viewsets import ModelViewSet


from device.models import (
    Device,
    DeviceInstallationPoint,
    DeviceRegistryNumber,
    DeviceType,
    DeviceMod,
    TypeToRegistry,
    DeviceVerification,
)
from device.serializers import (
    ShortDeviceSerializer,
    DeviceInstallationPointSerializer,
    DeviceRegistryNumberSerializer,
    DeviceTypeSerializer,
    DeviceModSerializer,
    TypeToRegistrySerializer,
    ShortDeviceVerificationSerializer,
)


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = ShortDeviceSerializer
    permission_classes = []


class DeviceInstallationPointViewSet(ModelViewSet):
    queryset = DeviceInstallationPoint.objects.all()
    serializer_class = DeviceInstallationPointSerializer
    permission_classes = []


class DeviceRegistryNumberViewSet(ModelViewSet):
    queryset = DeviceRegistryNumber.objects.all()
    serializer_class = DeviceRegistryNumberSerializer
    permission_classes = []


class DeviceTypeViewSet(ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = []


class DeviceModViewSet(ModelViewSet):
    queryset = DeviceMod.objects.all()
    serializer_class = DeviceModSerializer
    permission_classes = []


class TypeToRegistryViewSet(ModelViewSet):
    queryset = TypeToRegistry.objects.all()
    serializer_class = TypeToRegistrySerializer
    permission_classes = []


class DeviceVerificationViewSet(ModelViewSet):
    queryset = DeviceVerification.objects.all()
    serializer_class = ShortDeviceVerificationSerializer
    permission_classes = []
