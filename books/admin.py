from django.contrib import admin
from .models import Book
# Добавим-ка мы книги в админку
admin.site.register(Book)