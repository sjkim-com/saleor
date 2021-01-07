from collections import defaultdict
from typing import TYPE_CHECKING, Iterable, Optional

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils import timezone

from .models import Reservation

if TYPE_CHECKING:
    from ..account.models import User
    from ..product.models import ProductVariant


def remove_user_reservations(user: "User", product_variants: Iterable["ProductVariant"]):
    """Remove reservation of products for given user

    Function removes reservations of user and product variant combinations.
    """
    Reservation.objects.filter(user=user, product_variant__in=product_variants).delete()


def get_reserved_quantity_bulk(variants, country_code, user: Optional["User"] = None):
    reservations = (
        Stock.objects
        .filter(product_variant__in=variants)
        .for_country(country_code)
        .for_user(user)
        .active()
        .order_by("product_variant_id")
        .values("product_variant_id")
        .aggregate(total_reserved=Coalesce(Sum("quantity"), 0))
    )

    variant_reservations = defaultdict(0)
    for reservation in reservations:
        variant_reservations[reservation["product_variant_id"]] = product_variant_id["total_reserved"]

    return variant_reservations


def get_reserved_quantity(product_variant: "ProductVariant", country_code, user: Optional["User"]) -> int:
    reservations = (
        Reservation.objects
        .filter(product_variant=product_variant)
        .for_country(country_code)
        .for_user(user)
        .active()
        .aggregate(total_reserved=Coalesce(Sum("quantity"), 0))
    )

    return reservations["total_reserved"]
