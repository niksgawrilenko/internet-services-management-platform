from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from isp.forms import CityCreationForm, TariffCreationForm, CustomerCreationForm, AddressCreationForm
from isp.models import Customer, Address, City, Tariff


@login_required
def index(request):
    """View function for the home page of the site."""
    num_cities = City.objects.count()
    num_addresses = Address.objects.count()
    num_customers = Customer.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_cities": num_cities,
        "num_addresses": num_addresses,
        "num_customers": num_customers,
        "num_manufacturers": num_visits,
        "num_visits": num_visits + 1,
    }
    return render(request, "isp/index.html", context=context)


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    paginate_by = 10
    context_object_name = "cities"
    template_name = "isp/cities_list.html"


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    form_class = CityCreationForm
    success_url = reverse_lazy("isp:city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("isp:city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy("isp:city-list")


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    paginate_by = 10
    context_object_name = "customers"
    template_name = "isp/customers_list.html"


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = "isp/customer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["addresses_with_users"] = Address.objects.annotate(num_customers=Count('customers')).filter(num_customers__gt=0)
        return context


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerCreationForm
    success_url = reverse_lazy("isp:customers-detail")


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerCreationForm

    def get_success_url(self):
        return reverse_lazy("isp:customer-detail", kwargs={"pk": self.object.pk})


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Customer
    success_url = reverse_lazy("isp:customers")


class AddressListView(LoginRequiredMixin, generic.ListView):
    model = Address
    context_object_name = "addresses"
    template_name = "isp/addresses_list.html"


class AddressDetailView(LoginRequiredMixin, generic.DetailView):
    model = Address
    template_name = "isp/address_detail.html"


class AddressCreateView(LoginRequiredMixin, generic.CreateView):
    model = Address
    form_class = AddressCreationForm
    success_url = reverse_lazy("isp:addresses")


class AddressUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Address
    form_class = AddressCreationForm

    def get_success_url(self):
        return reverse_lazy("isp:address-detail", kwargs={"pk": self.object.pk})


class AddressDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Address
    success_url = reverse_lazy("isp:addresses")


class TariffListView(LoginRequiredMixin, generic.ListView):
    model = Tariff
    context_object_name = "tariffs"


class TariffCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tariff
    form_class = TariffCreationForm
    success_url = reverse_lazy("isp:tariff-list")


class TariffUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tariff
    fields = "__all__"
    success_url = reverse_lazy("isp:tariff-list")


class TariffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tariff
    success_url = reverse_lazy("isp:tariff-list")
