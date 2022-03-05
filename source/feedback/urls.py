from django.urls import path

from feedback.views import IndexView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'feedback'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='one_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review_add'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

]
