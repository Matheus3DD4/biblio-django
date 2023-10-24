from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from biblioteca.views import GenreViewSet, AuthorViewSet, TitleViewSet

router = DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"authores", AuthorViewSet)
router.register(r"titles", TitleViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
