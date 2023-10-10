from django.urls import path

from isp.cities.views import (
    CityListView,
    CityCreateView,
    CityUpdateView,
    CityDeleteView
)

urlpatterns = [
    path(
        "cities/",
        CityListView.as_view(),
        name="cities",
    ),
    path("cities/", CityListView.as_view(), name="city-list"),
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

]

app_name = "isp"
