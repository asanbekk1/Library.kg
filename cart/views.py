from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from django.http import HttpResponse
from .models import Book


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'total_price': total_price})

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    order = Order.objects.create(user=request.user)
    for item in items:
        OrderItem.objects.create(order=order, book=item.book, quantity=item.quantity)
    order.update_total_price()
    cart.books.clear()
    return redirect('order_detail', order_id=order.id)

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})
