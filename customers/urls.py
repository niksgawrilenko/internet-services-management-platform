from django.urls import path

from customers.views import (
    CustomerListView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerDeleteView,
    CustomerUpdateView
)

urlpatterns = [
    path(
        "",
        CustomerListView.as_view(),
        name="customers",
    ),
    path(
        "<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),
    path(
        "create/",
        CustomerCreateView.as_view(),
        name="customer-create",
    ),
    path(
        "<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    path(
        "<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customers-update"
    ),
]

app_name = "customers"
