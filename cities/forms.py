from django import forms

from cities.models import City


class CityCreationForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"


class CitySearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )
