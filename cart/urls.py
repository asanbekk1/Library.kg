from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_list, name='cart_list'),
    path('cart/<int:id>/', views.cart_detail, name='cart_detail'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
]