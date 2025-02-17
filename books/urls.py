from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:pk>/',views. BookDetailView.as_view(), name='book_detail'),
    path('books/',views. BookListView.as_view(), name='book_list'),





    path('about/', views.about_me, name='about_me'),
    path('photo/', views.text_and_photo, name='text_and_photo'),
    path('time/', views.system_time, name='system_time'),
]