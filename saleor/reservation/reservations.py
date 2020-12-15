from typing import TYPE_CHECKING, Iterable

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils import timezone

from .models import Reservation

if TYPE_CHECKING:
    from ..account.models import User
    from ..product.models import ProductVariant


def remove_user_stock_reservations(user: "User", product_variants: Iterable["ProductVariant"]):
    """Remove reservation of product for given user

    Function removes reservations of user and product variant combinations.
    """
    Reservation.objects.filter(user=user, product_variant__in=product_variants).delete()


def get_total_reserved_quantity(user: "User", product_variant: "ProductVariant") -> int:
    reservations = Reservation.objects.filter(
        product_variant=product_variant,
        expires__gt=timezone.now(),
    )

    if user.is_authenticated:
        reservations = reservations.exclude(user=user)

    results = reservations.aggregate(total_reserved=Coalesce(Sum("quantity"), 0))
    return results["total_reserved"]
