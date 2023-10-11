from django import forms
from django.contrib.auth.forms import UserCreationForm

from addresses.models import Address


class AddressCreationForm(forms.ModelForm):

    class Meta(UserCreationForm.Meta):
        model = Address
        fields = "__all__"


class AddressSearchForm(forms.Form):
    street = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by street..."})
    )
