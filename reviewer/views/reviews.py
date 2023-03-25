from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView

from reviewer.forms import ReviewForm
from reviewer.models import Review, Product


class ReviewCreateView(CreateView):
    template_name = "products/product.html"
    model = Review
    form_class = ReviewForm
    success_message = "Отзыв добавлен"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        review = form.save(commit=False)
        review.post = product
        review.author = self.request.user
        review.save()
        return redirect('reviewer:product_detail', pk=product.pk)


class ReviewDetailView(DetailView):
    template_name = 'reviews/review.html'
    model = Review

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.object.pk})


class ReviewUpdateView(UpdateView):
    template_name = "reviews/review_update.html"
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.object.pk})


class ReviewDeleteView(DeleteView):
    template_name = "reviews/review_confirm_delete.html"
    model = Review
    success_url = reverse_lazy("index")


class ReviewConfirmDeleteView(TemplateView):
    template_name = "reviews/review_confirm_delete.html"

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review"] = get_object_or_404(Review, pk=kwargs["pk"])
        context["review"].delete()
        return redirect("index")
