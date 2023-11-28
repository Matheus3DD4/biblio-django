from django.db import models
from .categoria import Categoria
from .autor import Autor

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="titulos"
    )
    autor = models.ForeignKey(
        Autor, on_delete=models.PROTECT, related_name="titulos"
    )

    def __str__(self):
        return self.titulo
