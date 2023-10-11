from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from addresses.models import Address
from cities.models import City
from customers.models import Customer


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
