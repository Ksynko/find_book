from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.name

class Page(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    chapter = models.ForeignKey(Chapter)

    def __str__(self):
        return str(self.number)
