from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone

from reviewer.manager import ProductManager


class CategoryChoice(TextChoices):
    OTHER = "other", "Other"
    FOOD = "food", "Food"
    PHARMACY = "pharmacy", "Pharmacy"
    CAR = "car", "Car"
    DEVICE = "device", "Device"


class Product(models.Model):
    title = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Title"
    )
    category = models.TextField(
        max_length=40,
        choices=CategoryChoice.choices,
        verbose_name="Category",
        default=CategoryChoice.OTHER,
        blank=False,
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="Description",
        default="No Description",
    )
    image = models.TextField(
        max_length=2000, null=True, blank=True, verbose_name="Image", default="https://icon-library.com/images/none-icon/none-icon-1.jpg"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date and time created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date and time updated"
    )
    is_deleted = models.BooleanField(verbose_name="Deleted", null=False, default=False)
    deleted_at = models.DateTimeField(
        verbose_name="Date and time deleted at", null=True, default=None
    )

    def __str__(self):
        return self.title

    objects = ProductManager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
