from django import forms
from feedback.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name_goods", "description", "picture")