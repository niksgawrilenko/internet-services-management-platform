from django.contrib import admin

from isp.addresses.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    search_fields = ("city__name", "street",)
    list_filter = ("city__name", "street", "connection_technology")
    list_display = (
        "get_city_name",
        "street",
        "building",
        "connection_technology"
    )

    def get_city_name(self, obj) -> None:
        return obj.city.name if obj.city else None

    get_city_name.short_description = "City Name"
