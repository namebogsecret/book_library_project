from django.db import models

class Book(models.Model):
    """
    Represents a book in the library.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author}"