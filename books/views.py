from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import BookModel

def book_list(request):
    books = BookModel.objects.all()
    context_object_name = {
        'books': books,
    }
    return render(request, 'book.html', context=context_object_name)

def book_detail(request, book_id):
    book = get_object_or_404(BookModel, pk=book_id)
    context_object_name = {
        'book': book,
    }
    return render(request, 'book_detail.html', context_object_name)








def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Айдар. Я разработчик Django!")

def text_and_photo(request):
    if request.method == 'GET':
        context = {
            'photo_url': 'path/to/photo.jpg',
            'text': 'Это пример текста с фото.',
        }
        return render(request, 'books/photo_page.html', context)

def system_time(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")
