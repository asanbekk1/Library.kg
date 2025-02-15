from django.db import models
from django.contrib.auth.models import User


# Модель книги
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title

# Модель для заказа
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Заказ #{self.id} - {self.user.username}"

# Модель для элемента корзины
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"

    def save(self, *args, **kwargs):
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)

# Модель для корзины
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='CartItem')

    def __str__(self):
        return f"Корзина {self.user.username}"

# Модель для элементов корзины
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
