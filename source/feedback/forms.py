from django import forms
from feedback.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name_goods", "description", "picture")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("mark", "text")
