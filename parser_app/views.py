from django.shortcuts import render,redirect
from django.views import generic
from . import models, forms

# PARSER FILM LIST
class ContentListView(generic.ListView):
    template_name = 'parser_app/content_list.html'
    context_object_name = 'content'
    model = models.ContentModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')


# FORM PARSER
class ContentFormView(generic.FormView):
    template_name = 'parser_app/parser_form.html'
    form_class = forms.ContentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('content_list')
        else:
            return super(ContentFormView, self).post(request, *args, **kwargs)





