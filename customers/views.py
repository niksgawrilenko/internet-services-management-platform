from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, QuerySet
from django.urls import reverse_lazy
from django.views import generic

from addresses.models import Address
from customers.forms import CustomerSearchForm, CustomerCreationForm
from customers.models import Customer


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    paginate_by = 10
    context_object_name = "customers"
    template_name = "customers/customers_list.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CustomerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Customer.objects.all()
        form = CustomerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["addresses_with_users"] = Address.objects.annotate(
            num_customers=Count("customers")
        ).filter(num_customers__gt=0)
        return context


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            "customers:customer-detail",
            kwargs={"pk": self.object.pk}
        )


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            "customers:customer-detail",
            kwargs={"pk": self.object.pk}
        )


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Customer
    success_url = reverse_lazy("customers:customers")
