from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def about_me(request):
    return HttpResponse("Меня зовут Айдар. Я разработчик Django!")

def text_and_photo(request):
    return render(request, 'books/photo_page.html')

def system_time(request):
    now = datetime.now()
    return HttpResponse(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

