from django.urls import path

from cities.views import (
    CityListView,
    CityCreateView,
    CityUpdateView,
    CityDeleteView
)

urlpatterns = [
    path(
        "",
        CityListView.as_view(),
        name="cities",
    ),
    path("", CityListView.as_view(), name="city-list"),
    path("create/", CityCreateView.as_view(), name="city-create"),
    path(
        "<int:pk>/update/",
        CityUpdateView.as_view(),
        name="city-update"
    ),
    path(
        "<int:pk>/delete/",
        CityDeleteView.as_view(),
        name="city-delete"
    ),

]

app_name = "cities"
