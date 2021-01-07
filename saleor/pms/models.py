from django.db import models

# Create your models here.
from ..ccs.models import Deliverypolicy, Control, Business, Store, User, \
    Offshop
# from ..dms.models import Template
from ..dms.models import Template


class Attribute(models.Model):
    attribute_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    attribute_type_cd = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store = models.ForeignKey('ccs.Store', models.DO_NOTHING)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('attribute_id', 'store_id'),)


class Attributelang(models.Model):
    attribute_id = models.CharField(max_length=100)
    # attribute_id = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='attribute_id', to_field='attribute_id')
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = (('attribute_id', 'lang_id'),)


class Attributevalue(models.Model):
    attribute_id = models.CharField(max_length=100)
    # attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    attribute_value = models.CharField(max_length=200)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_value = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING)

    class Meta:
        unique_together = (('attribute_id', 'attribute_value','store'),)


class Attributevaluedic(models.Model):
    attribute_id = models.CharField(max_length=100)
    # attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    dic_attribute_value = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    attribute_value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = (('attribute_id', 'dic_attribute_value'),)


class Barcode(models.Model):
    erp_barcode = models.CharField(primary_key=True, max_length=1000)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)



class Brand(models.Model):
    brand_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    erp_brand_id = models.CharField(max_length=100, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    logo_img = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    product_info = models.CharField(max_length=4000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)
    story = models.CharField(max_length=4000, blank=True, null=True)
    template = models.ForeignKey(Template, models.DO_NOTHING, blank=True, null=True)
    # template = models.ForeignKey(Template, models.DO_NOTHING, blank=True, null=True)



class Brandlang(models.Model):
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('brand', 'lang_id'),)

# TODO self reference migration
class Category(models.Model):
    category_id = models.CharField(max_length=100, primary_key=True)
    # TODO Foreign Key
    # category = models.OneToOneField('self', models.DO_NOTHING, primary_key=True, related_name='+')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    leaf_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)
    upper_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True,
                                       related_name='+')
    use_yn = models.CharField(max_length=1, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)


class Categoryattribute(models.Model):
    attribute_id = models.CharField(max_length=100)
    # attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    # category = models.CharField(max_length=100)
    # TODO Foreign Key
    category = models.ForeignKey(Category, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING)

    class Meta:
        unique_together = (('attribute_id', 'category'),)


class Categorylang(models.Model):
    # category = models.CharField(max_length=100)
    # TODO Foreign Key
    category = models.ForeignKey(Category, models.DO_NOTHING)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('category', 'lang_id'),)


class Categoryrating(models.Model):
    # category = models.CharField(max_length=100)
    # TODO Foreign Key
    category = models.ForeignKey(Category, models.DO_NOTHING)
    rating_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('category', 'rating_id'),)


class Epexcproduct(models.Model):
    exc_product_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    business_no = models.IntegerField(blank=True, null=True)
    exc_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)


class Inventory(models.Model):
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING
                                       )
    warehouse_id = models.CharField(max_length=100)
    business_no = models.IntegerField()
    provision_qty = models.IntegerField(blank=True, null=True)
    real_stock_qty = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=20, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = (('saleproduct', 'warehouse_id', 'business_no'),)


class Offshopstock(models.Model):
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING,
                                      db_column='offshop_no', to_field='offshop_no')
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    safe_stock_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         null=True)
    stock_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)

    class Meta:
        unique_together = (('offshop_no', 'saleproduct'),)


class Optionproduct(models.Model):
    option_product = models.ForeignKey('Product', models.DO_NOTHING, db_column='option_product_id'
                                          )
    product = models.ForeignKey('Product', models.DO_NOTHING, related_name='+')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('option_product', 'product'),)


class Pricereserve(models.Model):
    price_reserve_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    approval_dt = models.DateTimeField(blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    complete_dt = models.DateTimeField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    price_reserve_state_cd = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    regular_delivery_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    reject_reason = models.CharField(max_length=1000, blank=True, null=True)
    req_dt = models.DateTimeField(blank=True, null=True)
    reserve_dt = models.DateTimeField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)



class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    ad_copy = models.CharField(max_length=100, blank=True, null=True)
    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field='business_no',
                                    db_column='business_no', blank=True, null=True)
    business_product_id = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    # TODO Unblock Category
    claim_info = models.TextField(blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no', to_field='control_no',
                                   blank=True, null=True)
    delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    delivery_info = models.CharField(max_length=1000, blank=True, null=True)
    delivery_policy_no = models.ForeignKey(Deliverypolicy, models.DO_NOTHING,to_field='delivery_policy_no',
                                           db_column='delivery_policy_no', blank=True,
                                           null=True)
    detail = models.TextField(blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    erp_product_id = models.CharField(max_length=100, blank=True, null=True)
    fixed_delivery_yn = models.CharField(max_length=1, blank=True, null=True)
    gender_type_cd = models.CharField(max_length=100, blank=True, null=True)
    gift_yn = models.CharField(max_length=1, blank=True, null=True)
    global_ship_yn = models.CharField(max_length=1, blank=True, null=True)
    group1 = models.CharField(max_length=100, blank=True, null=True)
    group2 = models.CharField(max_length=100, blank=True, null=True)
    group3 = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.CharField(max_length=1000, blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    min_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    notice_confirm_dt = models.DateTimeField(blank=True, null=True)
    notice_confirm_id = models.CharField(max_length=100, blank=True, null=True)
    notice_confirm_yn = models.CharField(max_length=1, blank=True, null=True)
    offshop_img = models.CharField(max_length=100, blank=True, null=True)
    offshop_pickup_dc_rate = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    offshop_pickup_yn = models.CharField(max_length=1, blank=True, null=True)
    online_payment_yn = models.CharField(max_length=1, blank=True, null=True)
    option_yn = models.CharField(max_length=1, blank=True, null=True)
    out_send_dt = models.DateTimeField(blank=True, null=True)
    out_send_yn = models.CharField(max_length=1, blank=True, null=True)
    overseas_purchase_yn = models.CharField(max_length=1, blank=True, null=True)
    person_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                     null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    present_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                      null=True)
    price_apply_dt = models.DateTimeField(blank=True, null=True)
    product_notice_type_cd = models.CharField(max_length=100, blank=True, null=True)
    product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    regular_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    regular_delivery_max_cnt = models.IntegerField(blank=True, null=True)
    regular_delivery_max_qty = models.DecimalField(max_digits=10, decimal_places=0,
                                                   blank=True, null=True)
    regular_delivery_min_cnt = models.IntegerField(blank=True, null=True)
    regular_delivery_point_save_yn = models.CharField(max_length=1, blank=True,
                                                      null=True)
    regular_delivery_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    regular_delivery_yn = models.CharField(max_length=1, blank=True, null=True)
    reject_reason = models.CharField(max_length=1000, blank=True, null=True)
    reserve_delivery_dt = models.DateTimeField(blank=True, null=True)
    reserve_yn = models.CharField(max_length=1, blank=True, null=True)
    sale_end_dt = models.DateTimeField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    sale_start_dt = models.DateTimeField(blank=True, null=True)
    sale_state_cd = models.CharField(max_length=100, blank=True, null=True)
    search_exc_yn = models.CharField(max_length=1, blank=True, null=True)
    selling_point = models.CharField(max_length=4000, blank=True, null=True)
    sizechart_no = models.ForeignKey('Sizechart', models.DO_NOTHING, to_field='sizechart_no',
                                     db_column='sizechart_no', blank=True, null=True)
    stock_control_type_cd = models.CharField(max_length=100, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    theme_cd = models.CharField(max_length=100, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                   null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)
    wrap_volume = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    wrap_yn = models.CharField(max_length=1, blank=True, null=True)
    custom_id = models.CharField(max_length=100, blank=True, null=True)
    design_saleproduct = models.ForeignKey('self', models.DO_NOTHING, blank=True,
                                           null=True)
    vat_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)



class Productaddoption(models.Model):
    add_option_no = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_option_name = models.CharField(max_length=200, blank=True, null=True)
    add_option_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)
    product_add_option_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('add_option_no', 'product'),)


class Productaddoptionvalue(models.Model):
    add_option_no = models.IntegerField()
    # add_option_no = models.ForeignKey(Productaddoption, models.DO_NOTHING,to_field='add_option_no',
    #                                      db_column='add_option_no')
    add_option_value_no = models.IntegerField()
    product_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_option_value = models.CharField(max_length=1000, blank=True, null=True)
    add_option_value_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('add_option_no', 'add_option_value_no', 'product_id'),)


class Productattribute(models.Model):
    attribute_id = models.CharField(max_length=100)
    # attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    attribute_value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = (('attribute_id', 'product'),)


class Producthistory(models.Model):
    product_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)



class Productimg(models.Model):
    img_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    productimg_type_cd = models.CharField(max_length=100, blank=True, null=True)
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)



class Productlang(models.Model):
    lang_id = models.CharField(max_length=100)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    ad_copy = models.CharField(max_length=100, blank=True, null=True)
    attribute1 = models.CharField(max_length=200, blank=True, null=True)
    attribute2 = models.CharField(max_length=200, blank=True, null=True)
    attribute3 = models.CharField(max_length=200, blank=True, null=True)
    claim_info = models.TextField(blank=True, null=True)
    delivery_info = models.CharField(max_length=1000, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    group1 = models.CharField(max_length=100, blank=True, null=True)
    group2 = models.CharField(max_length=100, blank=True, null=True)
    group3 = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    selling_point = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'product'),)


class Productnotice(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    product_notice_field_id = models.CharField(max_length=100)
    product_notice_type_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        unique_together = (
        ('product', 'product_notice_field_id', 'product_notice_type_cd'),)


class Productnoticefield(models.Model):
    product_notice_field_id = models.CharField(max_length=100)
    product_notice_type_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    erp_field_name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('product_notice_field_id', 'product_notice_type_cd'),)


class Productnoticelang(models.Model):
    lang_id = models.CharField(max_length=20)
    product = models.ForeignKey(Productnotice, models.DO_NOTHING)
    product_notice_field_id = models.CharField(max_length=20)
    product_notice_type_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        unique_together = (
        ('lang_id', 'product', 'product_notice_field_id', 'product_notice_type_cd'),)


class Productoption(models.Model):
    option_no = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    attribute_id = models.CharField(max_length=20, blank=True, null=True)
    option_name = models.CharField(max_length=200, blank=True, null=True)
    product_option_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('option_no', 'product'),)


class Productoptionvalue(models.Model):
    option_no = models.IntegerField()
    # option_no = models.ForeignKey(Productoption, models.DO_NOTHING,
    #                                  db_column='option_no', to_field='option_no')
    option_value_no = models.IntegerField()
    product_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    attribute_value = models.CharField(max_length=200, blank=True, null=True)
    option_value = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('option_no', 'option_value_no', 'product_id'),)


class Productprice(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    coupon_id = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    family_coupon_id = models.CharField(max_length=100, blank=True, null=True)
    family_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    family_point_yn = models.CharField(max_length=1, blank=True, null=True)
    family_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                            null=True)
    gold_coupon_id = models.CharField(max_length=100, blank=True, null=True)
    gold_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    gold_point_yn = models.CharField(max_length=1, blank=True, null=True)
    gold_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    point_yn = models.CharField(max_length=1, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    silver_coupon_id = models.CharField(max_length=100, blank=True, null=True)
    silver_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    silver_point_yn = models.CharField(max_length=1, blank=True, null=True)
    silver_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                            null=True)
    vip_coupon_id = models.CharField(max_length=100, blank=True, null=True)
    vip_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    vip_point_yn = models.CharField(max_length=1, blank=True, null=True)
    vip_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    welcome_coupon_id = models.CharField(max_length=100, blank=True, null=True)
    welcome_delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    welcome_point_yn = models.CharField(max_length=1, blank=True, null=True)
    welcome_sale_price = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)



class Productqna(models.Model):
    product_qna_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answer_dt = models.DateTimeField(blank=True, null=True)
    answer_id = models.CharField(max_length=100, blank=True, null=True)
    confirm_dt = models.DateTimeField(blank=True, null=True)
    confirm_id = models.CharField(max_length=100, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email_yn = models.CharField(max_length=1, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_qna_state_cd = models.CharField(max_length=100, blank=True, null=True)
    product_qna_type_cd = models.CharField(max_length=100, blank=True, null=True)
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)
    secret_yn = models.CharField(max_length=1, blank=True, null=True)
    sms_yn = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)



class Productreserve(models.Model):
    product_reserve_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    ad_copy = models.CharField(max_length=100, blank=True, null=True)
    complete_dt = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_reserve_state_cd = models.CharField(max_length=100, blank=True, null=True)
    reserve_dt = models.DateTimeField()
    sale_state_cd = models.CharField(max_length=100, blank=True, null=True)



class Productsummary(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    order_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    rating = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)



class Recommendproduct(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING)
    recommend_product = models.ForeignKey(Product, models.DO_NOTHING,related_name='+')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    recommend_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('product', 'recommend_product'),)


class Review(models.Model):
    review_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    benefit_dt = models.DateTimeField(blank=True, null=True)
    best_yn = models.CharField(max_length=20, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    event_id = models.CharField(max_length=100, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    img3 = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    ps_register_end_dt = models.DateTimeField(blank=True, null=True)
    rating = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    saleproduct = models.ForeignKey('Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)



class Reviewrating(models.Model):
    rating_id = models.CharField(max_length=100)
    review_no = models.ForeignKey(Review, models.DO_NOTHING,to_field='review_no', db_column='review_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = (('rating_id', 'review_no'),)


class Saleproduct(models.Model):
    saleproduct_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    business_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    delivery_together_qty = models.DecimalField(max_digits=10, decimal_places=0,
                                                blank=True, null=True)
    erp_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey('Warehouselocation', models.DO_NOTHING, blank=True,
                                 null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    safe_stock_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         null=True)
    saleproduct_state_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    stock_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    warehouse_id = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)



class Saleproducthistory(models.Model):
    saleproduct_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    saleproduct = models.ForeignKey(Saleproduct, models.DO_NOTHING, blank=True,
                                    null=True)



class Saleproductlang(models.Model):
    lang_id = models.CharField(max_length=100)
    saleproduct = models.ForeignKey(Saleproduct, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'saleproduct'),)


class Saleproductoptionvalue(models.Model):
    saleproduct_option_value_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    option_no = models.IntegerField(blank=True, null=True)
    # option_no = models.ForeignKey(Productoptionvalue, models.DO_NOTHING,
    #                               db_column='option_no', to_field='option_no',blank=True, null=True)
    option_value_no = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    saleproduct = models.ForeignKey(Saleproduct, models.DO_NOTHING, blank=True,
                                    null=True)



class Saleproductpricereserve(models.Model):
    price_reserve_no = models.ForeignKey(Pricereserve, models.DO_NOTHING,
                                            db_column='price_reserve_no',
                                            to_field='price_reserve_no')
    saleproduct = models.ForeignKey(Saleproduct, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)

    class Meta:
        unique_together = (('price_reserve_no', 'saleproduct'),)


class Setproduct(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    sub_product = models.ForeignKey(Product, models.DO_NOTHING, related_name='+')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        unique_together = (('product', 'sub_product'),)


class Sizechart(models.Model):
    sizechart_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)



class Sizechartlang(models.Model):
    lang_id = models.CharField(max_length=100)
    sizechart_no = models.ForeignKey(Sizechart, models.DO_NOTHING,to_field='sizechart_no',
                                     db_column='sizechart_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'sizechart_no'),)


class Styleproduct(models.Model):
    style_product_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    style_product_color_cd = models.CharField(max_length=100, blank=True, null=True)
    style_product_item_cd = models.CharField(max_length=100, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)



class Warehouse(models.Model):
    warehouse_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    warehouse_state_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)



class Warehouselocation(models.Model):
    location_id = models.CharField(max_length=100)
    warehouse_id = models.ForeignKey(Warehouse, models.DO_NOTHING, db_column='warehouse_id', to_field='warehouse_id')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    location_use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('location_id', 'warehouse_id'),)


class Warehousestock(models.Model):
    warehouse_id = models.CharField(max_length=100)
    # warehouse = models.ForeignKey(Warehouselocation, models.DO_NOTHING
    #                                  )
    saleproduct = models.ForeignKey(Saleproduct, models.DO_NOTHING)
    safe_stock_qty = models.IntegerField()
    stock_qty = models.IntegerField()
    location_id = models.CharField(max_length=100, blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('warehouse_id', 'saleproduct'),)
