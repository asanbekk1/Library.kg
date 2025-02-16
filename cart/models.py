from django.db import models
from django.contrib.auth.models import User


# Модель книги
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


# Модель заказа
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('processing', 'Обрабатывается'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления заказа
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Общая стоимость заказа

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"


# Модель элемента заказа
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)  # Связь с книгой
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена на момент заказа

    def __str__(self):
        return f"{self.quantity} x {self.book.title} (Заказ #{self.order.id})"


# Модель корзины
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)  # Связь с книгой
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # Дата добавления в корзину

    def __str__(self):
        return f"{self.user.username}'s cart - {self.book.title}"

    def total_price(self):
        return self.quantity * self.book.price
