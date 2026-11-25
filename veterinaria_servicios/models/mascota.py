from django.db import models
from django.urls import reverse


class Mascota(models.Model):

    class Especie(models.TextChoices):
        PERRO = "perro", "Perro"
        GATO = "gato", "Gato"
        OTRA = "otra", "Otra"

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=Especie.choices)
    propietario = models.CharField(max_length=120)

    class Meta:
        ordering = ["nombre", "pk"]
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("mascota_detail", kwargs={"pk": self.pk})
