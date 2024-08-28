from .drf import (
    MenuSerializer,
    MenuCustomerSerializer,
    AddressesSerializer,
    ShortDeviceSerializer,
    ShortDeviceVerificationSerializer,
)
from .device import (
    DeviceSerializer,
    DeviceInstallationPointSerializer,
    DeviceRegistryNumberSerializer,
    DeviceTypeSerializer,
    DeviceModSerializer,
    TypeToRegistrySerializer,
    DeviceVerificationSerializer,
)

from .address import (
    AddressSerializer,
    OrganizationSerializer,
    UserToOrganizationSerializer,
    MeteringUnitSerializer,
)
