from django import forms
from . import models, parser_rezka

class ContentForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.ContentModel.objects.create(**i)