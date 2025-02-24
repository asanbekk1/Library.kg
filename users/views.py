from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from .forms import CustomRegisterForm
from .models import CustomUser

class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        experience = form.cleaned_data['experience']
        salary = self.request.salary  # Получаем зарплату из middleware
        self.object.salary = salary
        self.object.save()
        return response

class AuthLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return '/user_list/'

class AuthLogoutView(LogoutView):
    next_page = '/login/'

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = CustomUser

