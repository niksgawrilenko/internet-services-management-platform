from django.contrib import admin

from cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)
    list_display = ("name", "region", "country",)
