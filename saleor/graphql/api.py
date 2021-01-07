from graphene_federation import build_schema

from .account.schema import AccountMutations, AccountQueries
from .app.schema import AppMutations, AppQueries
# from .attribute.schema import AttributeMutations, AttributeQueries
from .ccs.schema import CcsMutations, CcsQueries
# from .channel.schema import ChannelMutations, ChannelQueries
from .checkout.schema import CheckoutMutations, CheckoutQueries
from .core.schema import CoreQueries
from .csv.schema import CsvMutations, CsvQueries
from .discount.schema import DiscountMutations, DiscountQueries
from .dms.schema import DmsQueries
from .giftcard.schema import GiftCardMutations, GiftCardQueries
from .invoice.schema import InvoiceMutations
from .menu.schema import MenuMutations, MenuQueries
from .meta.schema import MetaMutations
from .order.schema import OrderMutations, OrderQueries
from .page.schema import PageMutations, PageQueries
from .payment.schema import PaymentMutations, PaymentQueries
from .plugins.schema import PluginsMutations, PluginsQueries
from .pms.schema import PmsQueries
from .product.schema import ProductMutations, ProductQueries
from .shipping.schema import ShippingMutations, ShippingQueries
from .shop.schema import ShopMutations, ShopQueries
from .translations.schema import TranslationQueries
from .warehouse.schema import StockQueries, WarehouseMutations, WarehouseQueries
from .webhook.schema import WebhookMutations, WebhookQueries


class Query(
    AccountQueries,
    CcsQueries,
    AppQueries,
    # AttributeQueries,
    # ChannelQueries,
    CheckoutQueries,
    CoreQueries,
    CsvQueries,
    DiscountQueries,
    DmsQueries,
    PluginsQueries,
    GiftCardQueries,
    MenuQueries,
    OrderQueries,
    PageQueries,
    PaymentQueries,
    PmsQueries,
    ProductQueries,
    ShippingQueries,
    ShopQueries,
    StockQueries,
    TranslationQueries,
    WarehouseQueries,
    WebhookQueries,
):
    pass


class Mutation(
    AccountMutations,
    CcsMutations,
    AppMutations,
    # AttributeMutations,
    # ChannelMutations,
    CheckoutMutations,
    # CoreMutations,
    CsvMutations,
    DiscountMutations,
    PluginsMutations,
    GiftCardMutations,
    InvoiceMutations,
    MenuMutations,
    MetaMutations,
    OrderMutations,
    PageMutations,
    PaymentMutations,
    ProductMutations,
    ShippingMutations,
    ShopMutations,
    WarehouseMutations,
    WebhookMutations,
):
    pass


schema = build_schema(Query, mutation=Mutation)
