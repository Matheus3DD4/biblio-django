from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Autor
from biblioteca.serializers import AutorSerializer



class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer