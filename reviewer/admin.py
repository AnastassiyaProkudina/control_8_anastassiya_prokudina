from django.contrib import admin

from reviewer.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "description",
        "image",
        "created_at",
        "updated_at",
        "is_deleted",
        "deleted_at",
    )
    list_filter = ("title", "category")
    fields = ("title", "category", "description", "image")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    list_filter = ("id", "text", "created_at")
    fields = ("text",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

