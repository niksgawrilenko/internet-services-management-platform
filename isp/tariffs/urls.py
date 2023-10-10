from django.urls import path

from isp.tariffs.views import (
    TariffConnectView,
    TariffDeleteView,
    TariffUpdateView,
    TariffCreateView,
    TariffListView
)

urlpatterns = [
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
