from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from books.models import BookModel
from .forms import AddToCartForm



def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            quantity = form.cleaned_data['quantity']
            email = form.cleaned_data['email']
            cart_item = Cart(book=book, quantity=quantity, email=email)
            cart_item.save()
            return redirect('cart_list')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form})



def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart_list')


def cart_detail(request, id):
    cart = Cart.objects.get(id=id)
    return render(request, 'cart_detail.html', {'cart': cart})


def cart_list(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})