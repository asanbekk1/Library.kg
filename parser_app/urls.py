from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ContentListView.as_view(), name='content_list'),
    path('parsing/', views. ContentFormView.as_view(), name='parser'),
]