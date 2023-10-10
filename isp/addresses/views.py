from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from isp.addresses.forms import AddressSearchForm, AddressCreationForm
from isp.addresses.models import Address


class AddressListView(LoginRequiredMixin, generic.ListView):
    model = Address
    paginate_by = 10
    context_object_name = "addresses"
    template_name = "addresses/addresses_list.html"

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
    template_name = "addresses/address_detail.html"


class AddressCreateView(LoginRequiredMixin, generic.CreateView):
    model = Address
    form_class = AddressCreationForm
    success_url = reverse_lazy("isp:addresses")


class AddressUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Address
    form_class = AddressCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            "isp:address-detail",
            kwargs={"pk": self.object.pk}
        )


class AddressDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Address
    success_url = reverse_lazy("isp:addresses")


class AddressConnectView(LoginRequiredMixin, generic.View):
    def get(self, request, pk: int) -> HttpResponse:
        address = get_object_or_404(Address, pk=pk)

        address.customers.add(request.user)

        messages.success(
            request,
            f"You have been connected to address {address.building}."
        )
        return redirect(reverse("isp:addresses"))


def get(request: HttpRequest, pk: int) -> HttpResponse:
    address = get_object_or_404(Address, pk=pk)

    if request.user in address.customers.all():
        address.customers.remove(request.user)
        messages.success(
            request,
            f"You have been disconnected from address {address.building}."
        )
    else:
        messages.error(request, "You are not connected to this address.")

    return redirect(reverse("isp:addresses"))


class AddressDisconnectView(LoginRequiredMixin, generic.View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        address = get_object_or_404(Address, pk=pk)

        if request.user in address.customers.all():
            address.customers.remove(request.user)
            messages.success(
                request,
                f"You have been disconnected from address {address.building}."
            )
        else:
            messages.error(request, "You are not connected to this address.")

        return redirect(reverse("isp:addresses"))
