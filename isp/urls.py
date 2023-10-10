from django.urls import path

from isp.addresses.views import (
    AddressListView,
    AddressDetailView,
    AddressCreateView,
    AddressDeleteView,
    AddressUpdateView,
    AddressConnectView,
    AddressDisconnectView
)
from isp.cities.views import (
    CityListView,
    CityCreateView,
    CityUpdateView,
    CityDeleteView
)
from isp.customers.views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerUpdateView
)
from isp.tariffs.views import (
    TariffListView,
    TariffCreateView,
    TariffUpdateView,
    TariffDeleteView,
    TariffConnectView
)
from isp.views import index

urlpatterns = [
    path("", index, name="index"),
    path(
        "cities/",
        CityListView.as_view(),
        name="cities",
    ),
    path(
        "cities/",
        CityListView.as_view(),
        name="city-list",
    ),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path(
        "cities/<int:pk>/update/",
        CityUpdateView.as_view(),
        name="city-update"
    ),
    path(
        "cities/<int:pk>/delete/",
        CityDeleteView.as_view(),
        name="city-delete"
    ),
    path(
        "customers/",
        CustomerListView.as_view(),
        name="customers",
    ),
    path(
        "customers/",
        CustomerListView.as_view(),
        name="customers-list",
    ),
    path(
        "customers/<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),
    path(
        "customers/create/",
        CustomerCreateView.as_view(),
        name="customer-create",
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customers-update"
    ),
    path(
        "addresses/",
        AddressListView.as_view(),
        name="addresses",
    ),
    path(
        "addresses/",
        AddressListView.as_view(),
        name="address-list",
    ),
    path(
        "address/<int:pk>/",
        AddressDetailView.as_view(),
        name="address-detail"
    ),
    path(
        "address/create/",
        AddressCreateView.as_view(),
        name="address-create",
    ),
    path(
        "address/<int:pk>/delete/",
        AddressDeleteView.as_view(),
        name="address-delete",
    ),
    path(
        "address/<int:pk>/update/",
        AddressUpdateView.as_view(),
        name="address-update"
    ),
    path(
        "addresses/<int:pk>/connect/",
        AddressConnectView.as_view(),
        name="address-connect"
    ),
    path(
        "addresses/<int:pk>/disconnect/",
        AddressDisconnectView.as_view(),
        name="address-disconnect"
    ),
    path(
        "tariffs/",
        TariffListView.as_view(),
        name="tariffs",
    ),
    path("tariffs/", TariffListView.as_view(), name="tariff-list"),
    path("tariffs/create/", TariffCreateView.as_view(), name="tariff-create"),
    path(
        "tariffs/<int:pk>/update/",
        TariffUpdateView.as_view(),
        name="tariff-update"
    ),
    path(
        "tariffs/<int:pk>/delete/",
        TariffDeleteView.as_view(),
        name="tariff-delete"
    ),
    path(
        "tariffs/<int:pk>/connect/",
        TariffConnectView.as_view(),
        name="tariff-connect"
    ),
]

app_name = "isp"
