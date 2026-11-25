from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from .categoria import Categoria


class Servicio(models.Model):

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="servicios"
    )
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("servicio_detail", kwargs={"pk": self.pk})
