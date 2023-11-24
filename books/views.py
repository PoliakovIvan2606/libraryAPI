from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BooksAPIList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIUpdate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer