from django import forms
from .models import Cart

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['book_id', 'title', 'price', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Количество должно быть больше 0.")
        return quantity