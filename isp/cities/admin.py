from django.contrib import admin

from isp.cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)
    list_display = ("name", "region", "country",)
