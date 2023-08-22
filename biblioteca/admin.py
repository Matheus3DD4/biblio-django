from django.contrib import admin

from .models import Livro, Categoria, Autor

admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Autor)