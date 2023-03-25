from django import forms
from django.core.exceptions import ValidationError

from reviewer.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", "image", "description"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Title must be longer than two characters!")
        return title

