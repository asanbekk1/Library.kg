from books.models import Book
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

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
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"