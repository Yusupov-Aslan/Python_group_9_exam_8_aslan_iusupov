from django.contrib import admin
from django.contrib.auth.models import Permission

from feedback.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_goods', 'description']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name_goods', 'category', 'description', 'picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'mark', 'moderate']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Permission)
