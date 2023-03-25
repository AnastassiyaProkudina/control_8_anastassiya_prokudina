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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(
        max_length=30,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search Product...",
                "style": "border: solid #da7b93 2px; font-size: 16px; position: absolute;",
            }
        ),
    )
