from django.urls import path

from tariffs.views import (
    TariffConnectView,
    TariffUpdateView,
    TariffCreateView,
    TariffListView,
    TariffDeleteView
)

urlpatterns = [
    path(
        "",
        TariffListView.as_view(),
        name="tariffs",
    ),
    path("", TariffListView.as_view(), name="tariff-list"),
    path("create/", TariffCreateView.as_view(), name="tariff-create"),
    path(
        "<int:pk>/update/",
        TariffUpdateView.as_view(),
        name="tariff-update"
    ),
    path(
        "<int:pk>/delete/",
        TariffDeleteView.as_view(),
        name="tariff-delete"
    ),
    path(
        "<int:pk>/connect/",
        TariffConnectView.as_view(),
        name="tariff-connect"
    ),
]

app_name = "tariffs"
