from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import BookModel, Comment
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, ListView
from django.db.models import Q


class BookSearchView(ListView):
    model = BookModel
    template_name = 'book_search_results.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return BookModel.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return BookModel.objects.none()



class BookDetailView(DetailView, FormView):
    model = BookModel
    template_name = 'book_detail.html'
    form_class = CommentForm
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

    def form_valid(self, form):
        form.instance.book = self.get_object()
        form.save()
        return redirect('book_detail', id=self.get_object().id)


#def book_detail(request, id):
#    book = get_object_or_404(BookModel, id=id)
#    comments = book.comments.all()
#    form = CommentForm()
#
#    if request.method == 'POST':
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            form.instance.book = book
#            form.save()
#            return redirect('book_detail', id=id)
#
#    return render(request, 'book_detail.html', {'book': book, 'comments': comments, 'form': form})



class BookListView(ListView):
    model = BookModel
    template_name = 'book_list.html'
    context_object_name = 'books'




#def book_list(request):
#    books = BookModel.objects.all()
#    context_object_name = {
#        'books': books,
#    }
#    return render(request, 'book_list.html', context=context_object_name)



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



