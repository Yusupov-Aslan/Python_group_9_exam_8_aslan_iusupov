from django.contrib import admin
from feedback.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_goods', 'description']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name_goods', 'category', 'description', 'picture']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
