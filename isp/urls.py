from django.urls import path

from .views import index, CityListView, UserListView, AddressListView, TariffPlaneListView, CityDetailView, \
    CityCreateView, CityUpdateView, CityDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "cities/",
        CityListView.as_view(),
        name="cities",
    ),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/<int:pk>/", CityDetailView.as_view(), name="city-detail"),
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
        "tariff_planes/",
        TariffPlaneListView.as_view(),
        name="tariff_planes",
    ),
]

app_name = "isp"
