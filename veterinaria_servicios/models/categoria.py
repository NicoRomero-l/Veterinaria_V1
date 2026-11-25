from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("categoria_detail", kwargs={"pk": self.pk})
