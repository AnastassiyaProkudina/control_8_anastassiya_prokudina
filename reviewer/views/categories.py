from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from reviewer.forms import SimpleSearchForm
from reviewer.models import CategoryChoice, Product


def categories_list(request: WSGIRequest):
    form = SimpleSearchForm()
    title = request.GET.get("title")
    if title:
        products = (
            Product.objects.all()
            .filter(is_deleted=False, balance__gte=0, title=title)
            .order_by("category", "title")
        )
        context = {
            "products": products,
            "choices": CategoryChoice.choices,
            "form": form,
        }
        return render(request, "products/index.html", context=context)
    else:
        context = {"choices": CategoryChoice.choices, "form": form}
        return render(request, "categories/categories.html", context=context)


def category(request, pk):
    form = SimpleSearchForm()
    products = Product.objects.filter(is_deleted=False, category=pk)
    products.order_by("category", "title").values()
    if not products:
        message = f"You have no products in category {pk}"
        context = {"message": message, "form": form}
    else:
        message = f"You have {len(products)} product in category {pk}"
        context = {
            "products": products,
            "choices": CategoryChoice.choices,
            "message": message,
            "form": form,
        }
    return render(request, "products/index.html", context=context)
