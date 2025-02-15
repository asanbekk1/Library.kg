from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from books.models import Book
from .models import Order, OrderItem


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart', {})

    if str(book_id) in cart:
        cart[str(book_id)] += 1
    else:
        cart[str(book_id)] = 1

    request.session['cart'] = cart
    return JsonResponse({'status': 'success', 'cart': cart})


def view_cart(request):
    cart = request.session.get('cart', {})
    books = []
    total_price = 0

    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        total_price += book.price * quantity
        books.append({
            'book': book,
            'quantity': quantity,
            'total': book.price * quantity
        })

    context = {
        'books': books,
        'total_price': total_price
    }

    return render(request, 'cart/view_cart.html', context)


from django.shortcuts import redirect
from django.http import JsonResponse

def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})

    if str(book_id) in cart:
        del cart[str(book_id)]
        request.session['cart'] = cart
        return JsonResponse({'status': 'success', 'message': 'Книга удалена из корзины'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Книга не найдена в корзине'}, status=404)

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    order = Order.objects.create(user=request.user)
    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        OrderItem.objects.create(order=order, book=book, quantity=quantity)

    order.calculate_total_price()
    request.session['cart'] = {}

    return redirect('order_confirmation', order_id=order.id)


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'cart/order_confirmation.html', {'order': order})