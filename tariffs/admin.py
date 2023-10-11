from django.contrib import admin

from tariffs.models import Tariff


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("speed",)
    list_display = ("name", "speed", "price",)
