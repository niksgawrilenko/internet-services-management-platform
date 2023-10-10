from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.region}, {self.country}"

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"
