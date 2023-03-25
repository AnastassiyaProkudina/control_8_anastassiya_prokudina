from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from reviewer.forms import ProductForm, ReviewForm
from reviewer.models import Product, CategoryChoice, Review


class ProductDetail(DetailView):
    template_name = "products/product.html"
    model = Product
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews_ = Review.objects.filter(product_id=self.object.pk, is_deleted=False)
        products = Product.objects.filter(id=self.object.pk)
        context["products"] = products
        context["choices"] = CategoryChoice.choices
        context["form"] = self.form_class
        context["reviews"] = reviews_
        return context


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "products/product_create.html"
    model = Product
    form_class = ProductForm
    success_message = "Товар добавлен"

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "products/product_update.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "products/product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy("index")


class ProductConfirmDeleteView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "products/product_confirm_delete.html"
    success_message = "Товар удален"

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(Product, pk=kwargs["pk"])
        context["product"].delete()
        return redirect("index")

