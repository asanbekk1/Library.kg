from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите Email')
    phone = forms.CharField(required=True, label='Введите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите ваш возраст')
    gender = forms.ChoiceField(choices=GENDER, label='укажите ваш пол', required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone',
        )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user



