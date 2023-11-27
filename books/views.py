from django.core.cache import cache
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# def add_cache():
#     books = cache.get('books')
#     if not books:
#         a = Book.objects.all()
#         cache.set('books', a, 30)
#         return a
#     else:
#         return books

class BooksAPIList(generics.ListAPIView):
    """Контроллер для получения всего списка книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

class BookAPICreate(generics.CreateAPIView):
    """Контроллер для создании книги"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

class BookAPI(generics.RetrieveUpdateDestroyAPIView):
    """Контроллер для получения, изменения и удалении книги"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )