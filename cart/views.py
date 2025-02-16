from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Order, OrderItem, BookModel


# Добавить товар в корзину
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(BookModel, id=book_id)
        quantity = int(request.POST.get('quantity', 1))

        # Получаем или создаем элемент в корзине
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    return redirect('cart_detail')


# Удалить товар из корзины
@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart_detail')


# Просмотр корзины
@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})


# Оформление заказа
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart_detail')

    # Создаем заказ
    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0

    # Добавляем товары в заказ
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price=item.book.price
        )
        total_price += item.total_price()

    # Обновляем общую стоимость заказа
    order.total_price = total_price
    order.save()

    # Очищаем корзину
    cart_items.delete()

    return redirect('order_detail', order.id)


# Просмотр подробностей заказа
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_detail.html', {'order': order})
