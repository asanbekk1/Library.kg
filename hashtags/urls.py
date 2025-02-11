from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('children/', views.children_products, name='children_products'),
    path('teenage/', views.teenage_products, name='teenage_products'),
]