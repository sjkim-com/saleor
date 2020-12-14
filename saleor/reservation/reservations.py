from datetime import timedelta
from typing import TYPE_CHECKING

from django.db import transaction
from django.db.models import F
from django.utils import timezone

from .models import Reservation

if TYPE_CHECKING:
    from datetime import datetime

    from ..account.models import User
    from ..product.models import ProductVariant


RESERVATION_LENGTH = timedelta(minutes=20)


def _get_reservation_expiration() -> "datetime":
    return timezone.now() + RESERVATION_LENGTH


@transaction.atomic
def reserve_stock_for_user(user: "User", quantity: int, product_variant: "ProductVariant") -> "Reservation":
    """Reserve stock of given product variant for the user.

    Function lock for update all reservations for variant and user. Next, create or
    update quantity of existing reservation for the user.
    """
    reservation = (
        Reservation.objects.select_for_update(of=("self",))
        .filter(user=user, product_variant=product_variant)
        .first()
    )

    if reservation:
        updated_quantity = reservation.quantity + quantity
        reservation.quantity = F("quantity") + quantity
        reservation.expires = _get_reservation_expiration()
        reservation.save(update_fields=["quantity", "expires"])
        reservation.quantity = updated_quantity
    else:
        reservation = Reservation.objects.create(
            user=user,
            quantity=quantity,
            product_variant=product_variant,
            expires=_get_reservation_expiration(),
        )

    return reservation


def remove_user_reservation_of_stock(user: "User", product_variant: "ProductVariant") -> bool:
    """Remove reservation of product for given user

    Function removes reservations of user and production variant combinations.
    """
    rows_deleted = Reservation.objects.filter(user=user, product_variant=product_variant).delete()
    return bool(rows_deleted)
