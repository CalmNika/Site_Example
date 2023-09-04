from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    список = models.TextField()

book = Book(title="Примерная книга", author="Имя автора", publication_year=2022, список="Одиночная запись")
book.save()

data = ["Запись 1", "Запись 2", "Запись 3"]

for item in data:
    book = Book(title="Примерная книга", author="Имя автора", publication_year=2022, список=item)
    book.save()
