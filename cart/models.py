from django.db import models
from books.models import BookModel


# Модель корзины
class Cart(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    email = models.EmailField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title}"
