from rest_framework.serializers import ModelSerializer
from biblioteca.models import Titulo


class TituloSerializer(ModelSerializer):
    class Meta:
        model = Titulo
        fields = "__all__"


class TituloDetailSerializer(ModelSerializer):
    class Meta:
        model = Titulo
        fields = "__all__"
        depth = 1


class TituloListSerializer(ModelSerializer):
    class Meta:
        model = Titulo
        fields = ["id", "titulo", "autor"]
