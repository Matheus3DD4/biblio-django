from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Genre, Author, Title
from biblioteca.serializers import GenreSerializer, AuthorSerializer, TitleSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return Title