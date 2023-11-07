from rest_framework.serializers import ModelSerializer

from biblioteca.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


from biblioteca.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


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
