from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from isp.models import User, Address, Tariff, City


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("username", "phone",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)
    list_display = ("name", "region", "country",)


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("speed",)
    list_display = ("name", "speed", "price",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    search_fields = ("city__name", "street",)
    list_filter = ("city__name", "street", "connection_technology")
    list_display = ("get_city_name", "street", "building", "connection_technology")

    def get_city_name(self, obj) -> None:
        return obj.city.name if obj.city else None

    get_city_name.short_description = "City Name"
