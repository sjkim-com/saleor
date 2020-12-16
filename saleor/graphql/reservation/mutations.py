from datetime import timedelta

import graphene
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from ...product.models import ProductVariant
from ...reservation.error_codes import ReservationErrorCode
from ...reservation import models
from ..core.mutations import BaseMutation
from ..core.types.common import ReservationError
from ..product.types import ProductVariant
from .types import Reservation

RESERVATION_LENGTH = timedelta(minutes=20)
RESERVATION_SIZE_LIMIT = settings.MAX_CHECKOUT_LINE_QUANTITY


def _get_reservation_expiration() -> "datetime":
    return timezone.now() + RESERVATION_LENGTH


def check_reservation_quantity(quantity: int):
    """Check if reservation for given quantity is allowed."""
    if quantity < 1:
        raise ValidationError(
            {
                "quantity": ValidationError(
                    "The quantity should be higher than zero.",
                    code=ReservationErrorCode.ZERO_QUANTITY,
                )
            }
        )
    if quantity > RESERVATION_SIZE_LIMIT:
        raise ValidationError(
            {
                "quantity": ValidationError(
                    "Cannot reserve more than %d times this item."
                    "" % RESERVATION_SIZE_LIMIT,
                    code=ReservationErrorCode.QUANTITY_GREATER_THAN_LIMIT,
                )
            }
        )


@transaction.atomic
def reserve_stock_for_user(user: "User", quantity: int, product_variant: "ProductVariant") -> "Reservation":
    """Reserve stock of given product variant for the user.

    Function lock for update all reservations for variant and user. Next, create or
    update quantity of existing reservation for the user.
    """
    reservation = (
        models.Reservation.objects.select_for_update(of=("self",))
        .filter(user=user, product_variant=product_variant)
        .first()
    )

    if reservation:
        reservation.quantity = quantity
        reservation.expires = _get_reservation_expiration()
        reservation.save(update_fields=["quantity", "expires"])
    else:
        reservation = models.Reservation.objects.create(
            user=user,
            quantity=quantity,
            product_variant=product_variant,
            expires=_get_reservation_expiration(),
        )

    return reservation


class ReserveStock(BaseMutation):
    reservation = graphene.Field(
        Reservation, description="An reservation instance that was created or updated."
    )

    class Arguments:
        quantity = graphene.Int(required=True, description="The number of items to reserve.")
        variant_id = graphene.ID(required=True, description="ID of the product variant.")

    class Meta:
        description = "Reserve the stock for authenticated user checkout."
        error_type_class = ReservationError
        error_type_field = "reservation_errors"

    @classmethod
    def check_permissions(cls, context):
        return context.user.is_authenticated

    @classmethod
    def perform_mutation(cls, root, info, **data):
        check_reservation_quantity(data["quantity"])
        product_variant = cls.get_node_or_error(info, data["variant_id"], ProductVariant)

        reservation = reserve_stock_for_user(
            info.context.user,
            data["quantity"],
            product_variant
        )

        return ReserveStock(reservation=reservation)
