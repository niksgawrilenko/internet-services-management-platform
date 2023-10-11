from django.db import models

from cities.models import City
from customers.models import Customer


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255, unique=True)
    CONNECTION_TECHNOLOGIES = [
        ("FTTB", "FTTB"),
        ("FTTC", "FTTC"),
        ("FTTH", "FTTH"),
        ("DOCSIS", "DOCSIS"),
    ]
    connection_technology = models.CharField(
        max_length=10, choices=CONNECTION_TECHNOLOGIES
    )
    customers = models.ManyToManyField(Customer)

    def __str__(self) -> str:
        return (
            f"{self.city}, "
            f"{self.street}, "
            f"{self.building}. "
            f"{self.connection_technology}"
        )

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"
