from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.region}, {self.country}"

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"


class TariffPlane(models.Model):
    name = models.CharField(max_length=255)
    speed = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.speed} Mb/c, {self.price}$"


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    balance = models.FloatField(default=0.0)
    tariff_plane = models.ForeignKey(TariffPlane, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.username} "
            f"({self.first_name} "
            f"{self.last_name}), "
            f"{self.tariff_plane}), "
        )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


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
    users = models.ManyToManyField(User)

    def __str__(self):
        return (
            f"{self.city}, "
            f"{self.street}, "
            f"{self.building}. "
            f"{self.connection_technology}"
        )

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"
