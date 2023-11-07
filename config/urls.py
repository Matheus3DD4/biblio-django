from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from biblioteca.views import CategoriaViewSet, AutorViewSet, TituloViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"titulos", TituloViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
