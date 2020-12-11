from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models

if TYPE_CHECKING:
    # flake8: noqa
    from ..product.models import ProductVariant


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="reservations",
        on_delete=models.CASCADE,
    )
    expires = models.DateTimeField(null=False)
    product_variant = models.ForeignKey(
        "product.ProductVariant",
        null=False,
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [["user", "product_variant"]]
        ordering = ("pk",)
