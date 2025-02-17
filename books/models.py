from django.db import models
from django.contrib.auth.models import User



class BookModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateField(verbose_name="Дата публикации")
    cover_image = models.ImageField(upload_to='covers/', verbose_name="Обложка", null=True, blank=True)
    price = models.IntegerField(default=0)
    genre = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Comment(models.Model):
    book = models.ForeignKey(BookModel, related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    text = models.TextField()
    star = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.book.title}'
