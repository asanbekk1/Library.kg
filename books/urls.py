from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),


    path('about/', views.about_me, name='about_me'),
    path('photo/', views.text_and_photo, name='text_and_photo'),
    path('time/', views.system_time, name='system_time'),
]


