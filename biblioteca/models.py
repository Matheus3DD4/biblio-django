from django.db import models


class livro(models.Model):
    titulo = models.CharField(max_length=50)


def __str__(self):
    return self.livro
