from django.db import models


class Tariff(models.Model):
    name = models.CharField(max_length=255)
    speed = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.speed} Mb/c, {self.price}$"

    class Meta:
        verbose_name = "tariff"
        verbose_name_plural = "tariffs"
