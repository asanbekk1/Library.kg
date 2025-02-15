from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add price field

    def __str__(self):
        return self.title




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='books_orders')  # Связь с пользователем
    status = models.CharField(max_length=20, default='pending')  # Статус заказа: pending, completed
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания заказа
    updated_at = models.DateTimeField(auto_now=True)  # Время последнего обновления

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


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
    book = models.ForeignKey('books.Book', related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    text = models.TextField()
    star = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.book.title}'

