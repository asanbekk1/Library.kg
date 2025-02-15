from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('list/', views.book_list, name='book_list'),
    path('about/', views.about_me, name='about_me'),
    path('photo/', views.text_and_photo, name='text_and_photo'),
    path('time/', views.system_time, name='system_time'),
]