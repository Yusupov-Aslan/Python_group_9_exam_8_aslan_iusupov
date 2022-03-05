from django.contrib.auth.models import User
from django.db import models
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
# Create your models here.

CATEGORY_CHOICES = [("other", "Other"), ("laptops", "Laptops"), ("monitors", "Monitors"),
                    ("office_equipment", "Office equipment"), ("video_surveillance", "Video surveillance")]


@deconstructible
class MinValueValidator(BaseValidator):
    message = 'Значение "%(value)s" имеет значение %(show_value)d!Должно быть не меньше %(limit_value)d!'
    code = 'too_low'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return x


@deconstructible
class MaxValueValidator(BaseValidator):
    message = 'Убедитесь, что это значение не больше %(limit_value)d (у него %(show_value)d). '
    code = 'too_high'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return x


class Product(models.Model):
    name_goods = models.CharField(max_length=100, verbose_name='Наименование товара')
    category = models.CharField(max_length=20, default='other',
                                choices=CATEGORY_CHOICES, verbose_name='Категории')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст записи')
    picture = models.ImageField(verbose_name="Картинка", upload_to="pictures/", default='/pictures/product.jpg',
                                null=True, blank=True)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('feedback.Product', on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Продукт')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    mark = models.IntegerField(verbose_name="Оценка", validators=(MinValueValidator(1), MaxValueValidator(5),))
    moderate = models.BooleanField(verbose_name="Подтвержден", default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
