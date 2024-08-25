from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author")

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(str(book), "Test Book by Test Author")