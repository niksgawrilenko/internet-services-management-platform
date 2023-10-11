from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from isp.tariffs.models import Tariff


class Customer(AbstractUser):
    phone = models.CharField(max_length=20)
    balance = models.FloatField(default=0.0)
    tariff = models.ForeignKey(
        Tariff, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return (
            f"{self.username} "
            f"({self.first_name} "
            f"{self.last_name}), "
            f"{self.tariff}), "
        )

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def get_absolute_url(self) -> str:
        return reverse("isp:customer-detail", kwargs={"pk": self.pk})
