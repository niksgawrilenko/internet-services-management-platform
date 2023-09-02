from django.urls import path

from .views import index, CityListView, UserListView, AddressListView, TariffListView, \
    CityCreateView, CityUpdateView, CityDeleteView, TariffDeleteView, TariffUpdateView, TariffCreateView

urlpatterns = [
    path("", index, name="index"),
    path(
        "cities/",
        CityListView.as_view(),
        name="cities",
    ),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path("cities/<int:pk>/update/", CityUpdateView.as_view(), name="city-update"),
    path("cities/<int:pk>/delete/", CityDeleteView.as_view(), name="city-delete"),
    path(
        "users/",
        UserListView.as_view(),
        name="users",
    ),
    path(
        "addresses/",
        AddressListView.as_view(),
        name="addresses",
    ),
    path(
        "tariffs/",
        TariffListView.as_view(),
        name="tariffs",
    ),
    path("tariffs/", TariffListView.as_view(), name="tariff-list"),
    path("tariffs/create/", TariffCreateView.as_view(), name="tariff-create"),
    path("tariffs/<int:pk>/update/", TariffUpdateView.as_view(), name="tariff-update"),
    path("tariffs/<int:pk>/delete/", TariffDeleteView.as_view(), name="tariff-delete"),
]

app_name = "isp"
