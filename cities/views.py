from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from cities.forms import CitySearchForm, CityCreationForm
from cities.models import City


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    paginate_by = 10
    context_object_name = "cities"
    template_name = "cities/cities_list.html"

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
    success_url = reverse_lazy("cities:city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("cities:city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy("cities:city-list")
