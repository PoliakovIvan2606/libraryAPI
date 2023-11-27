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
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

class BookAPICreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

class BookAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )