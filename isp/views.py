from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from isp.forms import CityCreationForm
from isp.models import User, Address, City, TariffPlane


@login_required
def index(request):
    """View function for the home page of the site."""
    num_cities = City.objects.count()
    num_addresses = Address.objects.count()
    num_users = User.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_cities": num_cities,
        "num_addresses": num_addresses,
        "num_users": num_users,
        "num_manufacturers": num_visits,
        "num_visits": num_visits + 1,
    }
    return render(request, "isp/index.html", context=context)


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    paginate_by = 5
    context_object_name = "cities"
    template_name = "isp/cities_list.html"


class CityDetailView(LoginRequiredMixin, generic.DetailView):
    model = City


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


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = "users"
    template_name = "isp/users_list.html"


class AddressListView(LoginRequiredMixin, generic.ListView):
    model = Address
    context_object_name = "addresses"
    template_name = "isp/addresses_list.html"


class TariffPlaneListView(LoginRequiredMixin, generic.ListView):
    model = TariffPlane
    context_object_name = "tariff_planes"
    template_name = "isp/tariff_planes_list.html"
