from django.db import models
from .categoria import Categoria
from .autor import Autor
from uploader.models import Image

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="titulos"
    )
    autor = models.ForeignKey(
        Autor, on_delete=models.PROTECT, related_name="titulos"
    )
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.titulo
