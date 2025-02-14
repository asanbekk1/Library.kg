from django.db import models
from django.contrib.auth.models import User
from books.models import Book  

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    books = models.ManyToManyField(Book, through='OrderItem')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('Pending', 'В обработке'),
        ('Completed', 'Завершен'),
        ('Cancelled', 'Отменен'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    shipping_address = models.TextField(blank=True, null=True)

    payment_method = models.CharField(max_length=50, blank=True, null=True)

    is_paid = models.BooleanField(default=False)

    comment = models.TextField(blank=True, null=True)

    def calculate_total_price(self):
        self.total_price = sum(item.book.price * item.quantity for item in self.orderitem_set.all())
        self.save()

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem_set')

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title} (Заказ #{self.order.id})"