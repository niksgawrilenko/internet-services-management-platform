from django import forms
from django.contrib.auth.forms import UserCreationForm

from isp.customers.models import Customer


class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "phone",
            "email",
            "tariff"
        )


class CustomerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )
