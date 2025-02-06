from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateField(verbose_name="Дата публикации")
    cover_image = models.ImageField(upload_to='covers/', verbose_name="Обложка", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"