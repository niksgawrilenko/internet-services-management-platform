from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("username", "phone", "tariff")
