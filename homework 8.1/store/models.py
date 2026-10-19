from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название жанра")

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=150, verbose_name="Автор")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books', verbose_name="Жанр")

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="none")
    price = models.SmallIntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.book.title}"