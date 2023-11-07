from django.contrib import admin

from .models import Titulo, Categoria, Autor

admin.site.register(Titulo)
admin.site.register(Categoria)
admin.site.register(Autor)
