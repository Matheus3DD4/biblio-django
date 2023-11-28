from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Categoria
from biblioteca.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer