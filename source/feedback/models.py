from django.db import models

# Create your models here.

CATEGORY_CHOICES = [("other", "Other"), ("laptops", "Laptops"), ("monitors", "Monitors"),
                    ("office_equipment", "Office equipment"), ("video_surveillance", "Video surveillance")]


class Product(models.Model):
    name_goods = models.CharField(max_length=100, verbose_name='Наименование товара')
    category = models.CharField(max_length=20, default='other',
                                choices=CATEGORY_CHOICES, verbose_name='Категории')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст записи')
    picture = models.ImageField(verbose_name="Картинка", upload_to="pictures/", default='/pictures/product.jpg', null=True, blank=True)


class Review(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='', verbose_name='Автор')
    product = models.ForeignKey('feedback.Product', on_delete=models.CASCADE, related_name='review', verbose_name='Продукт')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    mark = models.IntegerField(verbose_name="Оценка")
    moderate = models.BooleanField(verbose_name="Модерирование")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
