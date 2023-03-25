from django.urls import path

from reviewer.views.base import IndexView, IndexRedirectView
from reviewer.views.categories import categories_list, category
from reviewer.views.products import *
from reviewer.views.reviews import ReviewCreateView, ReviewDetailView, ReviewDeleteView, ReviewUpdateView


app_name = "reviewer"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/", IndexRedirectView.as_view(), name="products_index_redirect"),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/<int:pk>/confirm_delete/",
        ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
    path("category/", categories_list, name="categories_list"),
    path("products/<pk>", category, name="category"),
    path("product/<int:pk>/review/add", ReviewCreateView.as_view(), name="review_create"),
    path("review/<pk>", ReviewDetailView.as_view(), name="review_detail"),
    path(
        "review/<int:pk>/update/", ReviewUpdateView.as_view(), name="review_update"
    ),
    path(
        "review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"
    ),
    path(
        "review/<int:pk>/confirm_delete/",
        ReviewDeleteView.as_view(),
        name="review_confirm_delete",
    ),

]
