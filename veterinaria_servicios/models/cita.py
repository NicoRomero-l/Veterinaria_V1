from django.conf import settings
from django.db import models
from django.urls import reverse

from .mascota import Mascota
from .servicio import Servicio


class Cita(models.Model):

    mascota = models.ForeignKey(
        Mascota, on_delete=models.PROTECT, related_name="citas"
    )
    servicios = models.ManyToManyField(Servicio, related_name="citas")
    fecha = models.DateField()
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="citas_creadas"
    )

    class Meta:
        ordering = ["-fecha", "-pk"]
        verbose_name = "cita"
        verbose_name_plural = "citas"

    def __str__(self):
        return f"{self.mascota} - {self.fecha:%d/%m/%Y}"

    def get_absolute_url(self):
        return reverse("cita_detail", kwargs={"pk": self.pk})
