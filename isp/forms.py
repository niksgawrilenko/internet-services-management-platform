from django import forms
from django.contrib.auth import get_user_model

from isp.models import City, Tariff


class CityCreationForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = City
        fields = "__all__"


class TariffCreationForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = "__all__"

