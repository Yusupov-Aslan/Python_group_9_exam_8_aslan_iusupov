from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from feedback.forms import ProductForm
from feedback.models import Product


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('category')


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "feedback.add_product"
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"

    def get_success_url(self):
        return reverse("feedback:one_product", kwargs={"pk": self.object.pk})


class ProductDetailView(DetailView):
    template_name = 'one_product.html'
    model = Product
    context_object_name = "product"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "feedback:change_product"
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("feedback:one_product", kwargs={"pk": self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "feedback:delete_product"
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('feedback:index')