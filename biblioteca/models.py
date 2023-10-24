from django.db import models

class Genre(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Author(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Title(models.Model):
    titulo = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="titles")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="titles")

    def __str__(self):
        return self.titulo

