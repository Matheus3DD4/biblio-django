from django.contrib import admin

from .models import Title, Genre, Author

admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Author)