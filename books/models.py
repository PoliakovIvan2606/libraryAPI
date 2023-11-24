from django.db import models

# Книги
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()
    ISBN = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.name