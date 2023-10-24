from rest_framework.serializers import ModelSerializer

from biblioteca.models import Genre

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

from biblioteca.models import Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

from biblioteca.models import Title

class TitleSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"

class TitleDetailSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"
        depth = 1

class TitleListSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = ["id", "title", "author"]