from django.urls import path

from .views import index, CityListView, UserListView, AddressListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "cities/",
        CityListView.as_view(),
        name="cities",
    ),
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
]

app_name = "isp"
