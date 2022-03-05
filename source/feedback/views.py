from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from feedback.forms import ProductForm, ReviewForm
from feedback.models import Product, Review


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('category')


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "feedback.add_product"
    model = Product
    form_class = ProductForm
    template_name = "product/product_create.html"

    def get_success_url(self):
        return reverse("feedback:one_product", kwargs={"pk": self.object.pk})


class ProductDetailView(DetailView):
    template_name = 'product/one_product.html'
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.get_object()
        ctx['average'] = product.get_average_mark()
        return ctx


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "feedback.change_product"
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("feedback:one_product", kwargs={"pk": self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "feedback.delete_product"
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('feedback:index')


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'review/review_create.html'
    form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product = self.get_object()
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            return redirect('feedback:one_product', pk=review.product.pk)
        else:
            return self.form_invalid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_update.html'

    def get_success_url(self):
        return reverse("feedback:one_product", kwargs={"pk": self.object.product.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.moderate = False
        self.object.save()
        return super().post(request, *args, **kwargs)


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'

    def get_success_url(self):
        return reverse('feedback:one_product', kwargs={"pk": self.object.product.pk})