from django import forms
from . import models, parser_mybook

class ContentForm(forms.Form):
    MEDIA_CHOICES = (
        ('mybook.ag', 'mybook.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.data['media_type'] == 'mybook.ag':
            mybook_book = parser_mybook.parsing_mybook()
            for i in mybook_book:
                models.ContentModel.objects.create(**i)