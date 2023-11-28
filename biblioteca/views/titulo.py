from rest_framework.viewsets import ModelViewSet
from biblioteca.models import Titulo
from biblioteca.serializers import TituloSerializer, TituloDetailSerializer, TituloListSerializer

class TituloViewSet(ModelViewSet):
    queryset = Titulo.objects.all()

    serializer_classes = {
        "list": TituloListSerializer,
        "retrieve": TituloDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TituloSerializer)
