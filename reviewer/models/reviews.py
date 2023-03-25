from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from reviewer.manager import ReviewManager


class Review(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="reviews",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        verbose_name="Товар",
        to="Product",
        related_name="reviews",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Комментарий", null=False, blank=False, max_length=20000
    )
    grade = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Grade",
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=None,
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
    objects = ReviewManager()

    def __str__(self):
        return self.text[:15]

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
