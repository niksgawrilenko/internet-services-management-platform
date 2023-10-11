from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from tariffs.forms import TariffSearchForm, TariffCreationForm
from tariffs.models import Tariff


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
    success_url = reverse_lazy("tariffs:tariff-list")


class TariffUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tariff
    fields = "__all__"
    success_url = reverse_lazy("tariffs:tariff-list")


class TariffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tariff
    success_url = reverse_lazy("tariffs:tariff-list")


class TariffConnectView(LoginRequiredMixin, generic.View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        tariff = get_object_or_404(Tariff, pk=pk)

        user = self.request.user
        user.tariff = tariff
        user.save()

        messages.success(
            request,
            f"Tariff {tariff.name} connected to {user.username}"
        )

        return redirect(reverse("tariffs:tariff-list"))
