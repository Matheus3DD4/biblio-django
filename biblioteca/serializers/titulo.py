from rest_framework.serializers import ModelSerializer, SlugRelatedField
from biblioteca.models import Titulo
from uploader.models import Image


class TituloSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
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
        fields = "__all__"
        depth = 1
