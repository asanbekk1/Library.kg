from django import forms
from .models import ContentModel

class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields = ['title', 'description', 'media_type', 'url']

def parser_data(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContentForm()
    return render(request, 'parser_form.html', {'form': form})