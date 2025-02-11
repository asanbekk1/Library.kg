from django import forms
from django.core.exceptions import ValidationError

from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'text', 'star']

    def clean(self):
        star = self.cleaned_data.get('star')
        if star < 1 or star > 5:
            raise ValidationError('Оценка должна быть от 1 до 5.')
        return star