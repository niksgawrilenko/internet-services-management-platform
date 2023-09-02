from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from isp.models import City, Tariff, Customer


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


class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + ("phone", "tariff")
