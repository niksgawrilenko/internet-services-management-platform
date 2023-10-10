from django.urls import path

from isp.customers.views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerUpdateView
)

urlpatterns = [
    path(
        "customers/",
        CustomerListView.as_view(),
        name="customers",
    ),
    path(
        "customers/<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),
    path(
        "customers/create/",
        CustomerCreateView.as_view(),
        name="customer-create",
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customers-update"
    ),
]

app_name = "isp"
