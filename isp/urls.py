from django.urls import path

from isp.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "isp"
