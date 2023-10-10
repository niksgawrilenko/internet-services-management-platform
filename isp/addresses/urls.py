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

urlpatterns = [

    path(
        "addresses/",
        AddressListView.as_view(),
        name="addresses",
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
]

app_name = "isp"
