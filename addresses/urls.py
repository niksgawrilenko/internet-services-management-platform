from django.urls import path

from addresses.views import (
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
        "",
        AddressListView.as_view(),
        name="addresses",
    ),
    path(
        "<int:pk>/",
        AddressDetailView.as_view(),
        name="address-detail"
    ),
    path(
        "create/",
        AddressCreateView.as_view(),
        name="address-create",
    ),
    path(
        "<int:pk>/delete/",
        AddressDeleteView.as_view(),
        name="address-delete",
    ),
    path(
        "<int:pk>/update/",
        AddressUpdateView.as_view(),
        name="address-update"
    ),
    path(
        "<int:pk>/connect/",
        AddressConnectView.as_view(),
        name="address-connect"
    ),
    path(
        "<int:pk>/disconnect/",
        AddressDisconnectView.as_view(),
        name="address-disconnect"
    ),
]

app_name = "addresses"
