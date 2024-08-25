from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve list of books or create a new book.
    
    get:
    Return a list of all the existing books.

    post:
    Create a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer