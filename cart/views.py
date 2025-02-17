from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from django.views import View
from books.models import BookModel
from .forms import AddToCartForm
from django.views.generic import DetailView, ListView


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        form = AddToCartForm()
        return render(request, 'add_to_cart.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddToCartForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            quantity = form.cleaned_data['quantity']
            email = form.cleaned_data['email']
            cart_item = Cart(book=book, quantity=quantity, email=email)
            cart_item.save()
            return redirect('cart_list')
        return render(request, 'add_to_cart.html', {'form': form})


#def add_to_cart(request):
#    if request.method == 'POST':
#        form = AddToCartForm(request.POST)
#        if form.is_valid():
#            book = form.cleaned_data['book']
#            quantity = form.cleaned_data['quantity']
#            email = form.cleaned_data['email']
#            cart_item = Cart(book=book, quantity=quantity, email=email)
#            cart_item.save()
#            return redirect('cart_list')
#    else:
#        form = AddToCartForm()
#    return render(request, 'add_to_cart.html', {'form': form})

class RemoveFromCartView(View):
    def post(self, request, cart_id, *args, **kwargs):
        cart_item = get_object_or_404(Cart, id=cart_id)
        cart_item.delete()
        return redirect('cart_list')


#def remove_from_cart(request, cart_id):
#    cart_item = get_object_or_404(Cart, id=cart_id)
#    cart_item.delete()
#    return redirect('cart_list')


class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart_detail.html'
    context_object_name = 'cart'

#def cart_detail(request, id):
#    cart = Cart.objects.get(id=id)
#    return render(request, 'cart_detail.html', {'cart': cart})


class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart_items'

#def cart_list(request):
#    cart_items = Cart.objects.all()
#    return render(request, 'cart.html', {'cart_items': cart_items})