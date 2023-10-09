from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from isp.forms import (
    CityCreationForm,
    TariffCreationForm,
    CustomerCreationForm,
    AddressCreationForm,
    CitySearchForm,
    CustomerSearchForm,
    AddressSearchForm,
    TariffSearchForm
)
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

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = CitySearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = City.objects.all()
        form = CitySearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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
    template_name = "isp/customer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["addresses_with_users"] = Address.objects.annotate(
            num_customers=Count("customers")
        ).filter(num_customers__gt=0)
        return context


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerCreationForm

    def get_success_url(self):
        return reverse_lazy("isp:customer-detail", kwargs={"pk": self.object.pk})


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
    paginate_by = 10
    context_object_name = "addresses"
    template_name = "isp/addresses_list.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        street = self.request.GET.get("street", "")

        context["search_form"] = AddressSearchForm(
            initial={"street": street}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Address.objects.all()
        form = AddressSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                street__icontains=form.cleaned_data["street"]
            )
        return queryset


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


class AddressConnectView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)

        address.customers.add(request.user)

        messages.success(request, f"You have been connected to address {address.building}.")
        return redirect(reverse("isp:addresses"))


class AddressDisconnectView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)

        if request.user in address.customers.all():
            address.customers.remove(request.user)
            messages.success(request, f"You have been disconnected from address {address.building}.")
        else:
            messages.error(request, "You are not connected to this address.")

        return redirect(reverse("isp:addresses"))


class TariffListView(LoginRequiredMixin, generic.ListView):
    model = Tariff
    paginate_by = 10
    context_object_name = "tariffs"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TariffSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Tariff.objects.all()
        form = TariffSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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


class TariffConnectView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        tariff = get_object_or_404(Tariff, pk=pk)

        user = self.request.user
        user.tariff = tariff
        user.save()

        messages.success(request, f"Tariff {tariff.name} connected to {user.username}")

        return redirect(reverse("isp:tariff-list"))
