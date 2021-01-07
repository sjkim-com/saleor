import graphene

from ... import graphql
from ...graphql.core.connection import CountableDjangoObjectType
from ...pms.models import *

class CategoryType(CountableDjangoObjectType):
    class Meta:
        model = Category

    category_id = graphene.String()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    leaf_yn = graphene.String()
    name = graphene.String()
    point_save_rate = graphene.Decimal()
    sort_no = graphene.Decimal()
    use_yn = graphene.String()
    store_id = graphene.String()
    # upper_category_id = graphene.Field(CategoryType)
    user_id = graphene.String()


class BrandType(CountableDjangoObjectType):
    class Meta:
        model = Brand

    ins_id = graphene.String()
    upd_id = graphene.String()
    detail = graphene.String()
    display_yn = graphene.String()
    erp_brand_id = graphene.String()
    img1 = graphene.String()
    img2 = graphene.String()
    logo_img = graphene.String()
    name = graphene.String()
    product_info = graphene.String()
    sort_no = graphene.Decimal()
    store_id = graphene.String()  # 既存 GCP FK : ccs_store
    story = graphene.String()
    template_id = graphene.String()  # 既存 GCP FK  : dms_template


class AttributeType(CountableDjangoObjectType):
    class Meta:
        model = Attribute

    attribute_id = graphene.String()  # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    attribute_type_cd = graphene.String()
    name = graphene.String()
    sort_no = graphene.Decimal()
    store_id = graphene.String()  # 既存 GCP PK
    use_yn = graphene.String()


class AttributevalueType(CountableDjangoObjectType):
    class Meta:
        model = Attributevalue

    attribute_id = graphene.String()  # 既存 GCP PK,FK
    attribute_value = graphene.String()  # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    add_value = graphene.String()
    name = graphene.String()
    sort_no = graphene.Decimal()
    use_yn = graphene.String()
    store_id = graphene.String()  # 既存 GCP PK, FK


class ProductOrgType(CountableDjangoObjectType):
    class Meta:
        model = Product

    product_id = graphene.String()  # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    ad_copy = graphene.String()
    attribute1 = graphene.String()
    attribute2 = graphene.String()
    attribute3 = graphene.String()
    brand_id = graphene.String()  # 既存 GCP FK : pms_brand
    business_no = graphene.Int()  # 既存 GCP FK : ccs_business
    business_product_id = graphene.String()
    category_id = graphene.String()  # 既存 GCP FK : pms_category
    claim_info = graphene.String()
    commission_rate = graphene.Decimal()
    control_no = graphene.Int()  # 既存 GCP FK : ccs_control
    delivery_fee_free_yn = graphene.String()
    delivery_info = graphene.String()
    delivery_policy_no = graphene.Int()  # 既存 GCP FK : ccs_deliverypolicy
    detail = graphene.String()
    display_yn = graphene.String()
    erp_product_id = graphene.String()
    fixed_delivery_yn = graphene.String()
    gender_type_cd = graphene.String()
    gift_yn = graphene.String()
    global_ship_yn = graphene.String()
    group1 = graphene.String()
    group2 = graphene.String()
    group3 = graphene.String()
    icon = graphene.String()
    keyword = graphene.String()
    list_price = graphene.Decimal()
    min_qty = graphene.Decimal()
    name = graphene.String()
    notice_confirm_id = graphene.String()
    notice_confirm_yn = graphene.String()
    offshop_img = graphene.String()
    offshop_pickup_dc_rate = graphene.Int()
    offshop_pickup_yn = graphene.String()
    online_payment_yn = graphene.String()
    option_yn = graphene.String()
    out_send_yn = graphene.String()
    overseas_purchase_yn = graphene.String()
    person_qty = graphene.Decimal()
    point_save_rate = graphene.Decimal()
    present_qty = graphene.Decimal()
    product_notice_type_cd = graphene.String()
    product_type_cd = graphene.String()
    regular_delivery_fee_free_yn = graphene.String()
    regular_delivery_max_cnt = graphene.Decimal()
    regular_delivery_max_qty = graphene.Decimal()
    regular_delivery_min_cnt = graphene.Decimal()
    regular_delivery_point_save_yn = graphene.String()
    regular_delivery_price = graphene.Decimal()
    regular_delivery_yn = graphene.String()
    reject_reason = graphene.String()
    reserve_yn = graphene.String()
    sale_price = graphene.Decimal()
    sale_state_cd = graphene.String()
    search_exc_yn = graphene.String()
    selling_point = graphene.String()
    sizechart_no = graphene.Int()  # 既存 GCP FK : pms_sizechart
    stock_control_type_cd = graphene.String()
    store_id = graphene.String()
    supply_price = graphene.Decimal()
    tax_type_cd = graphene.String()
    theme_cd = graphene.String()
    unit_qty = graphene.Decimal()
    use_yn = graphene.String()
    wrap_volume = graphene.Decimal()
    wrap_yn = graphene.String()
    custom_id = graphene.String()
    design_saleproduct_id = graphene.String()  # 既存 GCP FK : pms_product
    vat_rate = graphene.Decimal()


class ProductoptionType(CountableDjangoObjectType):
    class Meta:
        model = Productoption

    option_no = graphene.Int()  # 既存 GCP PK
    product_id = graphene.String()  # 既存 GCP PK, FK : pms_product
    ins_id = graphene.String()
    upd_id = graphene.String()
    attribute_id = graphene.String()
    option_name = graphene.String()
    product_option_type_cd = graphene.String()
    sort_no = graphene.Decimal()
    use_yn = graphene.String()


class ProductoptionvalueType(CountableDjangoObjectType):
    class Meta:
        model = Productoptionvalue

    option_no = graphene.Int()  # 既存 GCP PK, FK : pms_productoption
    option_value_no = graphene.Int()  # 既存 GCP PK
    product_id = graphene.String()  # 既存 GCP PK, FK : pms_productoption
    ins_id = graphene.String()
    upd_id = graphene.String()
    attribute_value = graphene.String()
    option_value = graphene.String()
    sort_no = graphene.Decimal()
    use_yn = graphene.String()


class SaleproductType(CountableDjangoObjectType):
    class Meta:
        model = Saleproduct

    saleproduct_id = graphene.String()   # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    add_sale_price = graphene.Decimal()
    business_saleproduct_id = graphene.String()
    delivery_together_qty = graphene.Int()
    erp_saleproduct_id = graphene.String()
    location_id = graphene.String()  # 既存 GCP FK : pms_warehouselocation
    name = graphene.String()
    safe_stock_qty = graphene.Decimal()
    saleproduct_state_cd = graphene.String()
    sort_no = graphene.Decimal()
    stock_qty = graphene.Decimal()
    warehouse_id = graphene.String()  # 既存 GCP FK : pms_warehouselocation
    product_id = graphene.String()  # 既存 GCP FK : pms_product
    store_id = graphene.String()


class SaleproductoptionvalueType(CountableDjangoObjectType):
    class Meta:
        model = Saleproductoptionvalue

    saleproduct_option_value_no = graphene.Int()  # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    option_no = graphene.Int()  # 既存 GCP FK : pms_productoptionvalue
    option_value_no = graphene.Int()  # 既存 GCP FK : pms_productoptionvalue
    product_id = graphene.String()  # 既存 GCP FK : pms_product, pms_productoptionvalue
    saleproduct_id = graphene.String()  # 既存 GCP FK : pms_saleproduct


class ProductnoticefieldType(CountableDjangoObjectType):
    class Meta:
        model = Productnoticefield

    product_notice_field_id = graphene.String()  # 既存 GCP PK
    product_notice_type_cd = graphene.String()  # 既存 GCP PK
    ins_id = graphene.String()
    upd_id = graphene.String()
    erp_field_name = graphene.String()
    note = graphene.String()
    sort_no = graphene.Decimal()
    title = graphene.String()


class ProductnoticeType(CountableDjangoObjectType):
    class Meta:
        model = Productnotice

    product_id = graphene.String()  # 既存 GCP PK, FK : pms_product
    product_notice_field_id = graphene.String()  # 既存 GCP PK, FK : pms_productnoticefield
    product_notice_type_cd = graphene.String()   # 既存 GCP PK, FK : pms_productnoticefield
    ins_id = graphene.String()
    upd_id = graphene.String()
    detail = graphene.String()


class WarehouseType(CountableDjangoObjectType):
    class Meta:
        model = Warehouse

    warehouse_id = graphene.String()   # 既存 GCP PK
    name = graphene.String()
    country_id = graphene.String()
    zip_cd = graphene.String()
    address1 = graphene.String()
    address2 = graphene.String()
    address3 = graphene.String()
    address4 = graphene.String()
    warehouse_state_cd = graphene.String()
    ins_id = graphene.String()
    sort_no = graphene.Decimal()
    upd_id = graphene.String()
    store_id = graphene.String()


class WarehousestockType(CountableDjangoObjectType):
    class Meta:
        model = Warehousestock

    warehouse_id = graphene.String()  # 既存 GCP PK, FK : pms_warehouse, pms_warehouselocation
    saleproduct_id = graphene.String()  # 既存 GCP PK, FK : pms_saleproduct
    safe_stock_qty = graphene.Decimal()
    stock_qty = graphene.Decimal()
    location_id = graphene.String()  # 既存 GCP FK : pms_warehouselocation
    ins_id = graphene.String()
    upd_id = graphene.String()


class WarehouselocationType(CountableDjangoObjectType):
    class Meta:
        model = Warehouselocation

    location_id = graphene.String()  # 既存 GCP PK
    warehouse_id = graphene.String()  # 既存 GCP PK, FK : pms_warehouse
    ins_id = graphene.String()
    upd_id = graphene.String()
    location_use_yn = graphene.String()
