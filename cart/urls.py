from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views. CartListView.as_view(), name='cart_list'),
    path('cart/<int:pk>/',views. CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/',views. AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_id>/',views. RemoveFromCartView.as_view(), name='remove_from_cart'),
]