from django import forms

from isp.tariffs.models import Tariff


class TariffCreationForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = "__all__"


class TariffSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )
