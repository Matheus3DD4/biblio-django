from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Categoria, Autor, Titulo
from biblioteca.serializers import (
    CategoriaSerializer,
    AutorSerializer,
    TituloSerializer,
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class TituloViewSet(ModelViewSet):
    queryset = Titulo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return Titulo
