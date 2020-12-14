import graphene

from ...product.models import ProductVariant
from ...reservation.reservations import (
    remove_user_reservation_of_stock, reserve_stock_for_user
)
from ..core.mutations import BaseMutation
from ..product.types import ProductVariant
from .types import Reservation


class ReserveStock(BaseMutation):
    reservation = graphene.Field(
        Reservation, description="An reservation instance that was created or updated."
    )

    class Arguments:
        quantity = graphene.Int(required=True, description="The number of items to reserve.")
        variant_id = graphene.ID(required=True, description="ID of the product variant.")

    class Meta:
        description = "Reserve the stock for authenticated user checkout."
        #error_type_class = AppError
        error_type_field = "reservation_errors"

    @classmethod
    def check_permissions(cls, context):
        return context.user.is_authenticated

    @classmethod
    def perform_mutation(cls, root, info, **data):
        product_variant = cls.get_node_or_error(info, data["variant_id"], ProductVariant)

        reservation = reserve_stock_for_user(
            info.context.user,
            data["quantity"],
            product_variant
        )

        return ReserveStock(reservation=reservation)
