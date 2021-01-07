from django.db import models

# Create your models here.
from ..ccs.models import Channel, Store, Site, Offshop
from ..mms.models import Member


class Cart(models.Model):
    cart_product_no = models.OneToOneField('self', models.DO_NOTHING,
                                           db_column='cart_product_no',
                                           primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    cart_id = models.CharField(max_length=100, blank=True, null=True)
    cart_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    cart_state_cd = models.CharField(max_length=100, blank=True, null=True)
    cart_type_cd = models.CharField(max_length=100, blank=True, null=True)
    channel_no = models.ForeignKey(Channel, models.DO_NOTHING, db_column='channel_no',
                                   blank=True, null=True)
    coupon_no = models.ForeignKey('sps.Coupon', models.DO_NOTHING, db_column='coupon_no',
                                  blank=True, null=True)
    deal_no = models.ForeignKey('sps.Deal', models.DO_NOTHING, db_column='deal_no',
                                blank=True, null=True)
    delivery_cnt = models.IntegerField(blank=True, null=True)
    delivery_period_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_period_value = models.IntegerField(blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    keep_yn = models.CharField(max_length=1, blank=True, null=True)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, db_column='offshop_no',
                                   blank=True, null=True)
    product = models.ForeignKey('pms.Product', models.DO_NOTHING, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    regular_delivery_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    saleproduct = models.ForeignKey('pms.Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)
    set_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    style_no = models.IntegerField(blank=True, null=True)
    total_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)
    upper_cart_product_no = models.ForeignKey('self', models.DO_NOTHING,
                                              db_column='upper_cart_product_no',
                                              blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'oms_cart'


class Claim(models.Model):
    claim_no = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    accept_dt = models.DateTimeField(blank=True, null=True)
    cancel_dt = models.DateTimeField(blank=True, null=True)
    claim_state_cd = models.CharField(max_length=100, blank=True, null=True)
    claim_type_cd = models.CharField(max_length=100, blank=True, null=True)
    complete_dt = models.DateTimeField(blank=True, null=True)
    order_coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                     blank=True, null=True)
    plus_coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                    blank=True, null=True)
    product_coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                       blank=True, null=True)
    refund_product_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    req_dt = models.DateTimeField()
    return_pickup_type_cd = models.CharField(max_length=100, blank=True, null=True)
    withdraw_reason = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_claim'
        unique_together = (('claim_no', 'order'),)


class Claimcoupon(models.Model):
    order = models.OneToOneField(Claim, models.DO_NOTHING, primary_key=True)
    claim_no = models.IntegerField()
    coupon_issue_no = models.ForeignKey('Ordercoupon', models.DO_NOTHING,
                                        db_column='coupon_issue_no')
    coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                               blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_claimcoupon'
        unique_together = (('order', 'claim_no', 'coupon_issue_no'),)


class Claimdelivery(models.Model):
    claim_no = models.OneToOneField(Claim, models.DO_NOTHING, db_column='claim_no',
                                    primary_key=True)
    delivery_address_no = models.ForeignKey('Delivery', models.DO_NOTHING,
                                            db_column='delivery_address_no')
    delivery_policy_no = models.IntegerField()
    order_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=200, blank=True, null=True)
    delivery_coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                        blank=True, null=True)
    delivery_service_cd = models.CharField(max_length=100, blank=True, null=True)
    exchange_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    order_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    refund_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                              blank=True, null=True)
    refund_exchange_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                                       blank=True, null=True)
    refund_return_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                                     blank=True, null=True)
    refund_wrap_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    return_address1 = models.CharField(max_length=300, blank=True, null=True)
    return_address2 = models.CharField(max_length=300, blank=True, null=True)
    return_address3 = models.CharField(max_length=200, blank=True, null=True)
    return_address4 = models.CharField(max_length=200, blank=True, null=True)
    return_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                              blank=True, null=True)
    return_email = models.CharField(max_length=100, blank=True, null=True)
    return_phone1 = models.CharField(max_length=100, blank=True, null=True)
    return_phone2 = models.CharField(max_length=100, blank=True, null=True)
    return_zip_cd = models.CharField(max_length=200, blank=True, null=True)
    wrap_coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                    blank=True, null=True)
    return_name1 = models.CharField(max_length=200, blank=True, null=True)
    return_name2 = models.CharField(max_length=200, blank=True, null=True)
    return_name3 = models.CharField(max_length=200, blank=True, null=True)
    return_name4 = models.CharField(max_length=200, blank=True, null=True)
    return_phone3 = models.CharField(max_length=100, blank=True, null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    in_country_id = models.CharField(max_length=100, blank=True, null=True)
    in_zip_cd = models.CharField(max_length=200, blank=True, null=True)
    in_address1 = models.CharField(max_length=300, blank=True, null=True)
    in_address2 = models.CharField(max_length=300, blank=True, null=True)
    in_address3 = models.CharField(max_length=200, blank=True, null=True)
    in_address4 = models.CharField(max_length=200, blank=True, null=True)
    warehouse_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_claimdelivery'
        unique_together = (
        ('claim_no', 'delivery_address_no', 'delivery_policy_no', 'order_id'),)


class Claimproduct(models.Model):
    claim_no = models.OneToOneField(Claim, models.DO_NOTHING, db_column='claim_no',
                                    primary_key=True)
    order = models.ForeignKey('Orderproduct', models.DO_NOTHING)
    order_product_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    claim_product_state_cd = models.CharField(max_length=100, blank=True, null=True)
    claim_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    claim_reason = models.CharField(max_length=1000, blank=True, null=True)
    claim_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    return_dt = models.DateTimeField(blank=True, null=True)
    return_order_dt = models.DateTimeField(blank=True, null=True)
    refund_product_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    without_return_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_claimproduct'
        unique_together = (('claim_no', 'order', 'order_product_no'),)


class Delivery(models.Model):
    delivery_address_no = models.OneToOneField('Deliveryaddress', models.DO_NOTHING,
                                               db_column='delivery_address_no',
                                               primary_key=True)
    delivery_policy_no = models.IntegerField()
    order_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    apply_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    apply_wrap_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    delivery_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    delivery_coupon_issue_no = models.ForeignKey('oms.Ordercoupon', models.DO_NOTHING,
                                                 db_column='delivery_coupon_issue_no',
                                                 blank=True, null=True, related_name='+')
    delivery_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    delivery_service_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_type_cd = models.CharField(max_length=100, blank=True, null=True)
    min_delivery_free_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    order_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    order_wrap_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    wrap_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    wrap_coupon_issue_no = models.ForeignKey('oms.Ordercoupon', models.DO_NOTHING,
                                             db_column='wrap_coupon_issue_no',
                                             blank=True, null=True, related_name='+')
    wrap_together_yn = models.CharField(max_length=1, blank=True, null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    gift_yn = models.CharField(max_length=1, blank=True, null=True)
    gift_msg = models.CharField(max_length=4000, blank=True, null=True)
    apply_delivery_fee_tax = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    apply_wrap_fee_tax = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_delivery'
        unique_together = (('delivery_address_no', 'delivery_policy_no', 'order_id'),)


class Deliveryaddress(models.Model):
    delivery_address_no = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=300, blank=True, null=True)
    address2 = models.CharField(max_length=300, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=200, blank=True, null=True)
    delivery_address_type_cd = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, db_column='offshop_no',
                                   blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    pickup_delivery_dt = models.DateTimeField(blank=True, null=True)
    pickup_reserve_dt = models.DateTimeField(blank=True, null=True)
    zip_cd = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_deliveryaddress'
        unique_together = (('delivery_address_no', 'order'),)


class Deliveryaddresshistory(models.Model):
    delivery_address_history_no = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Deliveryaddress, models.DO_NOTHING, blank=True, null=True)
    delivery_address_no = models.IntegerField(blank=True, null=True)
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200, blank=True, null=True)
    name3 = models.CharField(max_length=200, blank=True, null=True)
    name4 = models.CharField(max_length=200, blank=True, null=True)
    country_no = models.CharField(max_length=200, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    delivery_address_type_cd = models.CharField(max_length=100)
    pickup_reserve_dt = models.DateTimeField(blank=True, null=True)
    pickup_delivery_dt = models.DateTimeField(blank=True, null=True)
    country_id = models.CharField(max_length=200, blank=True, null=True)
    zip_cd = models.CharField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=300, blank=True, null=True)
    address2 = models.CharField(max_length=300, blank=True, null=True)
    address3 = models.CharField(max_length=300, blank=True, null=True)
    address4 = models.CharField(max_length=300, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_deliveryaddresshistory'


class Deliverytracking(models.Model):
    delivery_service_time = models.DateTimeField(primary_key=True)
    delivery_step_cd = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    logistics_inout_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_detail = models.CharField(max_length=255, blank=True, null=True)
    delivery_location = models.CharField(max_length=100, blank=True, null=True)
    deliveryman_mobile_no = models.CharField(max_length=50, blank=True, null=True)
    office_phone_no = models.CharField(max_length=50, blank=True, null=True)
    receiver_address = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    tracker_reg_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oms_deliverytracking'
        unique_together = (('delivery_service_time', 'delivery_step_cd', 'invoice_no',
                            'logistics_inout_no'),)


class Erpif(models.Model):
    erp_if_no = models.AutoField(primary_key=True)
    erp_product_no = models.IntegerField()
    order = models.ForeignKey('Orderproduct', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    business_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_no = models.IntegerField(blank=True, null=True)
    cash_refund_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    claim_no = models.ForeignKey(Claim, models.DO_NOTHING, db_column='claim_no',
                                 blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    deal_type_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_address_no = models.ForeignKey(Delivery, models.DO_NOTHING,
                                            db_column='delivery_address_no', blank=True,
                                            null=True)
    delivery_policy_no = models.IntegerField(blank=True, null=True)
    deposit_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    deposit_refund_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    erp_business_id = models.CharField(max_length=100, blank=True, null=True)
    erp_color_id = models.CharField(max_length=100, blank=True, null=True)
    erp_order_type_cd = models.CharField(max_length=100, blank=True, null=True)
    erp_product_id = models.CharField(max_length=100, blank=True, null=True)
    erp_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    erp_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    erp_size_id = models.CharField(max_length=100, blank=True, null=True)
    fixed_dt = models.DateTimeField(blank=True, null=True)
    order_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                              blank=True, null=True)
    order_dt = models.DateTimeField(blank=True, null=True)
    order_product_no = models.IntegerField(blank=True, null=True)
    own_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    payment_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_method_cd = models.CharField(max_length=100, blank=True, null=True)
    plus_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    purchase_yn = models.CharField(max_length=1, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sale_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    sale_type_cd = models.CharField(max_length=100, blank=True, null=True)
    saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    saleproduct_name = models.CharField(max_length=1000, blank=True, null=True)
    save_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    total_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)
    use_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'oms_erpif'
        unique_together = (('erp_if_no', 'erp_product_no', 'order'),)


class Logistics(models.Model):
    logistics_inout_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    bad_in_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                     null=True)
    cancel_delivery_qty = models.DecimalField(max_digits=10, decimal_places=0,
                                              blank=True, null=True)
    cancel_delivery_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    claim_no = models.ForeignKey(Claimproduct, models.DO_NOTHING, db_column='claim_no',
                                 blank=True, null=True)
    complete_dt = models.DateTimeField(blank=True, null=True)
    delivery_cancel_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_if_type_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_order = models.IntegerField(blank=True, null=True)
    delivery_service_cd = models.CharField(max_length=100, blank=True, null=True)
    good_in_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                      null=True)
    in_reserve_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         null=True)
    invoice_dt = models.DateTimeField(blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    logistics_state_cd = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, db_column='offshop_no',
                                   blank=True, null=True)
    order = models.ForeignKey('Orderproduct', models.DO_NOTHING, blank=True, null=True)
    order_product_no = models.IntegerField(blank=True, null=True)
    out_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    out_reserve_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                          null=True)
    saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    tracking_if_result = models.CharField(max_length=1000, blank=True, null=True)
    tracking_if_yn = models.CharField(max_length=1, blank=True, null=True)
    virtual_in_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         null=True)
    virtual_out_qty = models.DecimalField(max_digits=22, decimal_places=0, blank=True,
                                          null=True)
    warehouse_inout_type_cd = models.CharField(max_length=100, blank=True, null=True)
    wrap_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                   null=True)
    delivery_no = models.IntegerField(blank=True, null=True)
    warehouse_id = models.CharField(max_length=20, blank=True, null=True)
    location_id = models.CharField(max_length=20, blank=True, null=True)
    transfer_out_no = models.IntegerField(blank=True, null=True)
    inout_reason_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_logistics'


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    cancel_dt = models.DateTimeField(blank=True, null=True)
    channel_no = models.ForeignKey(Channel, models.DO_NOTHING, db_column='channel_no',
                                   blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    delivery_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gift_img_type_cd = models.CharField(max_length=100, blank=True, null=True)
    gift_msg = models.CharField(max_length=4000, blank=True, null=True)
    gift_name = models.CharField(max_length=100, blank=True, null=True)
    gift_phone = models.CharField(max_length=100, blank=True, null=True)
    member_grade_cd = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)
    order_delivery_state_cd = models.CharField(max_length=100, blank=True, null=True)
    order_dt = models.DateTimeField()
    order_pwd = models.CharField(max_length=1000, blank=True, null=True)
    order_state_cd = models.CharField(max_length=100, blank=True, null=True)
    order_type_cd = models.CharField(max_length=100, blank=True, null=True)
    payment_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    phone1 = models.CharField(max_length=200, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    point = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    site = models.ForeignKey(Site, models.DO_NOTHING, blank=True, null=True)
    site_mem_id = models.CharField(max_length=100, blank=True, null=True)
    site_order_id = models.CharField(max_length=100, blank=True, null=True)
    site_type_cd = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)
    zip_cd = models.CharField(max_length=200, blank=True, null=True)
    order_error_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order'


class Orderb2E(models.Model):
    order_b2e_no = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    business_condition = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_type = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    erp_business_id = models.CharField(max_length=100, blank=True, null=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=100, blank=True, null=True)
    rep_name = models.CharField(max_length=100, blank=True, null=True)
    tax_bill_issue_yn = models.CharField(max_length=1, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderb2e'
        unique_together = (('order_b2e_no', 'order_id'),)


class Ordercoupon(models.Model):
    coupon_issue_no = models.OneToOneField('sps.Couponissue', models.DO_NOTHING,
                                           db_column='coupon_issue_no',
                                           primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    affiliate_yn = models.CharField(max_length=1, blank=True, null=True)
    business_burden_rate = models.DecimalField(max_digits=14, decimal_places=2,
                                               blank=True, null=True)
    business_no = models.IntegerField(blank=True, null=True)
    coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    coupon_dc_cancel_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                               blank=True, null=True)
    coupon_type_cd = models.CharField(max_length=100, blank=True, null=True)
    dc_apply_type_cd = models.CharField(max_length=100, blank=True, null=True)
    dc_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    max_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    min_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    order_coupon_state_cd = models.CharField(max_length=100, blank=True, null=True)
    single_apply_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_ordercoupon'
        unique_together = (('coupon_issue_no', 'order'),)


class Orderhistory(models.Model):
    order_history_no = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    order_history_type_cd = models.CharField(max_length=100)
    order_history_detail = models.CharField(max_length=4000, blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderhistory'


class Ordermemo(models.Model):
    order = models.OneToOneField('Orderproduct', models.DO_NOTHING, primary_key=True)
    order_memo_no = models.IntegerField()
    order_product_no = models.IntegerField(blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_ordermemo'
        unique_together = (('order', 'order_memo_no'),)


class Orderpresent(models.Model):
    order = models.OneToOneField(Order, models.DO_NOTHING, primary_key=True)
    present_no = models.IntegerField()
    name = models.CharField(max_length=100)
    present_type_cd = models.CharField(max_length=100)
    present_select_type_cd = models.CharField(max_length=100)
    select_qty = models.IntegerField(blank=True, null=True)
    min_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    max_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderpresent'
        unique_together = (('order', 'present_no'),)


class Orderpresentproduct(models.Model):
    order = models.OneToOneField('Orderproduct', models.DO_NOTHING, primary_key=True)
    present_no = models.IntegerField()
    order_product_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderpresentproduct'
        unique_together = (('order', 'present_no', 'order_product_no'),)


class Orderproduct(models.Model):
    order = models.OneToOneField(Orderpresent, models.DO_NOTHING, primary_key=True)
    order_product_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    brand_id = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_no = models.IntegerField(blank=True, null=True)
    business_phone = models.CharField(max_length=100, blank=True, null=True)
    business_product_id = models.CharField(max_length=100, blank=True, null=True)
    business_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    calibrate_order_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    calibrate_plus_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    calibrate_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    calibrate_product_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                   blank=True, null=True)
    calibrate_sale_price = models.DecimalField(max_digits=14, decimal_places=2,
                                               blank=True, null=True)
    cancel_delivery_reason_cd = models.CharField(max_length=1, blank=True, null=True)
    cancel_dt = models.DateTimeField(blank=True, null=True)
    cancel_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                     null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    claim_no = models.ForeignKey(Claim, models.DO_NOTHING, db_column='claim_no',
                                 blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    confirm_dt = models.DateTimeField(blank=True, null=True)
    deal_name = models.CharField(max_length=200, blank=True, null=True)
    deal_no = models.IntegerField(blank=True, null=True)
    deal_product_no = models.IntegerField(blank=True, null=True)
    deal_type_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_address_no = models.ForeignKey(Deliveryaddress, models.DO_NOTHING,
                                            db_column='delivery_address_no', blank=True,
                                            null=True)
    delivery_cancel_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_dt = models.DateTimeField(blank=True, null=True)
    delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    delivery_order_dt = models.DateTimeField(blank=True, null=True)
    delivery_policy_no = models.IntegerField(blank=True, null=True)
    delivery_reserve_dt = models.DateTimeField(blank=True, null=True)
    erp_business_id = models.CharField(max_length=100, blank=True, null=True)
    erp_product_id = models.CharField(max_length=100, blank=True, null=True)
    erp_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    fixed_delivery_yn = models.CharField(max_length=1, blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    offshop_no = models.IntegerField(blank=True, null=True)
    option_yn = models.CharField(max_length=1, blank=True, null=True)
    order_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                              blank=True, null=True)
    order_coupon_issue_no = models.ForeignKey(Ordercoupon, models.DO_NOTHING,
                                              db_column='order_coupon_issue_no',
                                              blank=True, null=True, related_name='+')
    order_delivery_type_cd = models.CharField(max_length=100, blank=True, null=True)
    order_dt = models.DateTimeField(blank=True, null=True)
    order_product_state_cd = models.CharField(max_length=100, blank=True, null=True)
    order_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    order_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    origin_order_product_no = models.IntegerField(blank=True, null=True)
    out_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    overseas_purchase_yn = models.CharField(max_length=1, blank=True, null=True)
    payment_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_dt = models.DateTimeField(blank=True, null=True)
    personal_customs_code = models.CharField(max_length=20, blank=True, null=True)
    plus_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                             blank=True, null=True)
    plus_coupon_issue_no = models.ForeignKey(Ordercoupon, models.DO_NOTHING,
                                             db_column='plus_coupon_issue_no',
                                             blank=True, null=True, related_name='+')
    plus_single_apply_yn = models.CharField(max_length=1, blank=True, null=True)
    point_name = models.CharField(max_length=100, blank=True, null=True)
    point_save_no = models.ForeignKey('sps.Pointsave', models.DO_NOTHING,
                                      db_column='point_save_no', blank=True, null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    point_type_cd = models.CharField(max_length=100, blank=True, null=True)
    point_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    present_max_order_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    present_min_order_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    present_name = models.CharField(max_length=100, blank=True, null=True)
    present_no = models.IntegerField(blank=True, null=True)
    product_coupon_dc_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    product_coupon_issue_no = models.ForeignKey(Ordercoupon, models.DO_NOTHING,
                                                db_column='product_coupon_issue_no',
                                                blank=True, null=True, related_name='+')
    product = models.ForeignKey('pms.Product', models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    product_notice_type_cd = models.CharField(max_length=100, blank=True, null=True)
    product_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    product_single_apply_yn = models.CharField(max_length=1, blank=True, null=True)
    purchase_yn = models.CharField(max_length=1, blank=True, null=True)
    reserve_yn = models.CharField(max_length=1, blank=True, null=True)
    return_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                     null=True)
    sabang_order_id = models.CharField(max_length=100, blank=True, null=True)
    sabang_product_id = models.CharField(max_length=100, blank=True, null=True)
    sabang_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    sale_type_cd = models.CharField(max_length=100, blank=True, null=True)
    saleproduct = models.ForeignKey('pms.Saleproduct', models.DO_NOTHING, blank=True,
                                    null=True)
    saleproduct_name = models.CharField(max_length=1000, blank=True, null=True)
    save_dt = models.DateTimeField(blank=True, null=True)
    send_error_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    send_error_yn = models.CharField(max_length=1, blank=True, null=True)
    set_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    ship_dt = models.DateTimeField(blank=True, null=True)
    site_product_id = models.CharField(max_length=100, blank=True, null=True)
    site_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    style_no = models.IntegerField(blank=True, null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    total_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    total_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)
    upper_order_product_no = models.IntegerField(blank=True, null=True)
    virtual_out_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                          null=True)
    virtual_return_qty = models.DecimalField(max_digits=10, decimal_places=0,
                                             blank=True, null=True)
    wrap_volume = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    wrap_yn = models.CharField(max_length=1, blank=True, null=True)
    order_product_error_cd = models.CharField(max_length=100, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    present_type_cd = models.CharField(max_length=100, blank=True, null=True)
    present_select_type_cd = models.CharField(max_length=100, blank=True, null=True)
    present_select_qty = models.IntegerField(blank=True, null=True)
    calibrate_tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderproduct'
        unique_together = (('order', 'order_product_no'),)


class Orderproductaddoption(models.Model):
    order_product_add_option_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_option_name = models.CharField(max_length=200, blank=True, null=True)
    add_option_no = models.IntegerField(blank=True, null=True)
    add_option_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)
    add_option_value = models.CharField(max_length=1000, blank=True, null=True)
    add_option_value_no = models.IntegerField(blank=True, null=True)
    add_option_value_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    cart_product_no = models.ForeignKey(Cart, models.DO_NOTHING,
                                        db_column='cart_product_no', blank=True,
                                        null=True)
    order = models.ForeignKey(Orderproduct, models.DO_NOTHING, blank=True, null=True)
    order_product_no = models.IntegerField(blank=True, null=True)
    product_add_option_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_orderproductaddoption'


class Payment(models.Model):
    payment_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    account_no = models.CharField(max_length=100, blank=True, null=True)
    cancel_dt = models.DateTimeField(blank=True, null=True)
    cash_receipt_approval_no = models.CharField(max_length=100, blank=True, null=True)
    cash_receipt_type_cd = models.CharField(max_length=100, blank=True, null=True)
    claim_no = models.ForeignKey(Claim, models.DO_NOTHING, db_column='claim_no',
                                 blank=True, null=True)
    credit_payment_type_cd = models.CharField(max_length=100, blank=True, null=True)
    creditcard_no = models.CharField(max_length=100, blank=True, null=True)
    deposit_no = models.IntegerField(blank=True, null=True)
    depositor_name = models.CharField(max_length=100, blank=True, null=True)
    escrow_if_result = models.CharField(max_length=4000, blank=True, null=True)
    escrow_if_yn = models.CharField(max_length=1, blank=True, null=True)
    escrow_yn = models.CharField(max_length=1, blank=True, null=True)
    installment_cnt = models.IntegerField(blank=True, null=True)
    interest_free_yn = models.CharField(max_length=1, blank=True, null=True)
    major_payment_yn = models.CharField(max_length=1, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=100, blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    partial_cancel_yn = models.CharField(max_length=1, blank=True, null=True)
    payment_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_business_cd = models.CharField(max_length=100, blank=True, null=True)
    payment_business_nm = models.CharField(max_length=100, blank=True, null=True)
    payment_dt = models.DateTimeField(blank=True, null=True)
    payment_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_method_cd = models.CharField(max_length=100, blank=True, null=True)
    payment_state_cd = models.CharField(max_length=100, blank=True, null=True)
    payment_type_cd = models.CharField(max_length=100, blank=True, null=True)
    pg_approval_no = models.CharField(max_length=100, blank=True, null=True)
    pg_cancel_no = models.CharField(max_length=100, blank=True, null=True)
    pg_shop_id = models.CharField(max_length=100, blank=True, null=True)
    refund_account_info = models.CharField(max_length=1000, blank=True, null=True)
    refund_account_no = models.CharField(max_length=100, blank=True, null=True)
    refund_reason_cd = models.CharField(max_length=100, blank=True, null=True)
    tax_bill_req_yn = models.CharField(max_length=1, blank=True, null=True)
    virtual_account_deposit_end_dt = models.DateTimeField(blank=True, null=True)
    virtual_account_deposit_order = models.CharField(max_length=3, blank=True,
                                                     null=True)
    tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    net_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'oms_payment'


class Paymentif(models.Model):
    order_id = models.CharField(primary_key=True, max_length=100)
    payment_if_no = models.IntegerField()
    payment_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    payment_if_result = models.CharField(max_length=1000, blank=True, null=True)
    payment_req_data = models.TextField(blank=True, null=True)
    payment_return_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_paymentif'
        unique_together = (('order_id', 'payment_if_no', 'payment_no'),)


class Paymentsettle(models.Model):
    payment_method_cd = models.CharField(primary_key=True, max_length=100)
    pg_approval_no = models.CharField(max_length=100)
    pg_cancel_no = models.CharField(max_length=100)
    pg_shop_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    payment_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_dt = models.DateTimeField()
    payment_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    payment_type_cd = models.CharField(max_length=100, blank=True, null=True)
    pg_order_id = models.CharField(max_length=100, blank=True, null=True)
    settle_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_paymentsettle'
        unique_together = (
        ('payment_method_cd', 'pg_approval_no', 'pg_cancel_no', 'pg_shop_id'),)


class Pickup(models.Model):
    pickup_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    pickup_req_dt = models.DateTimeField(blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_pickup'


class Pickupproduct(models.Model):
    pickup = models.OneToOneField(Pickup, models.DO_NOTHING, primary_key=True)
    product_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    brand_id = models.CharField(max_length=100, blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    erp_color_id = models.CharField(max_length=100, blank=True, null=True)
    erp_product_id = models.CharField(max_length=100, blank=True, null=True)
    erp_saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    erp_size_id = models.CharField(max_length=100, blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    offshop_no = models.IntegerField(blank=True, null=True)
    order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)
    order_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    pickup_cancel_dt = models.DateTimeField(blank=True, null=True)
    pickup_delivery_dt = models.DateTimeField(blank=True, null=True)
    pickup_product_state_cd = models.CharField(max_length=100, blank=True, null=True)
    pickup_req_dt = models.DateTimeField(blank=True, null=True)
    pickup_reserve_dt = models.DateTimeField(blank=True, null=True)
    pos_mid = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    saleproduct_name = models.CharField(max_length=200, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    total_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                           null=True)

    class Meta:
        managed = False
        db_table = 'oms_pickupproduct'
        unique_together = (('pickup', 'product_no'),)


class Pointif(models.Model):
    point_if_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    acml_pint = models.CharField(max_length=10, blank=True, null=True)
    acml_tgt_amt = models.CharField(max_length=10, blank=True, null=True)
    mmb_cert_dv_cd = models.CharField(max_length=1, blank=True, null=True)
    mmb_cert_dv_vlu = models.CharField(max_length=20, blank=True, null=True)
    org_apv_dt = models.CharField(max_length=8, blank=True, null=True)
    org_apv_no = models.CharField(max_length=10, blank=True, null=True)
    org_uniq_rcgn_no = models.CharField(max_length=50, blank=True, null=True)
    pint_acml_typ_cd = models.CharField(max_length=2, blank=True, null=True)
    pint_use_typ_cd = models.CharField(max_length=2, blank=True, null=True)
    point_if_req_data = models.TextField(blank=True, null=True)
    point_if_return_data = models.TextField(blank=True, null=True)
    tot_sel_amt = models.CharField(max_length=10, blank=True, null=True)
    trsc_biz_dv_cd = models.CharField(max_length=2, blank=True, null=True)
    trsc_dt = models.CharField(max_length=8, blank=True, null=True)
    trsc_hr = models.CharField(max_length=6, blank=True, null=True)
    trsc_rsn_cd = models.CharField(max_length=4, blank=True, null=True)
    trsc_typ_cd = models.CharField(max_length=3, blank=True, null=True)
    uniq_rcgn_no = models.CharField(max_length=50, blank=True, null=True)
    use_pint = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_pointif'


class Posorder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    avail_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    card_issue_no = models.CharField(max_length=20, blank=True, null=True)
    member_no = models.CharField(max_length=70, blank=True, null=True)
    offshop_no = models.IntegerField(blank=True, null=True)
    order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)
    order_dt = models.DateTimeField()
    product_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    save_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    use_point = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'oms_posorder'


class Posorderproduct(models.Model):
    erp_saleproduct_id = models.CharField(primary_key=True, max_length=100)
    order = models.ForeignKey(Posorder, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                    null=True)
    order_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    tax_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_posorderproduct'
        unique_together = (('erp_saleproduct_id', 'order'),)


class Presentproduct(models.Model):
    order = models.OneToOneField(Orderproduct, models.DO_NOTHING, primary_key=True)
    order_product_no = models.IntegerField()
    present_no = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    present_type_cd = models.CharField(max_length=100)
    present_select_type_cd = models.CharField(max_length=100)
    select_qty = models.IntegerField(blank=True, null=True)
    min_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    max_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=20, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_presentproduct'
        unique_together = (('order', 'order_product_no'),)


class Regulardelivery(models.Model):
    regular_delivery_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    delivery_address1 = models.CharField(max_length=200, blank=True, null=True)
    delivery_address2 = models.CharField(max_length=200, blank=True, null=True)
    delivery_address3 = models.CharField(max_length=200, blank=True, null=True)
    delivery_address4 = models.CharField(max_length=200, blank=True, null=True)
    delivery_country_no = models.CharField(max_length=20, blank=True, null=True)
    delivery_name1 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name2 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name3 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name4 = models.CharField(max_length=100, blank=True, null=True)
    delivery_phone1 = models.CharField(max_length=100, blank=True, null=True)
    delivery_phone2 = models.CharField(max_length=100, blank=True, null=True)
    delivery_phone3 = models.CharField(max_length=100, blank=True, null=True)
    delivery_zip_cd = models.CharField(max_length=20, blank=True, null=True)
    device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_regulardelivery'


class Regulardeliveryproduct(models.Model):
    delivery_product_no = models.OneToOneField('self', models.DO_NOTHING,
                                               db_column='delivery_product_no',
                                               primary_key=True)
    regular_delivery = models.ForeignKey(Regulardelivery, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    delivery_cnt = models.IntegerField(blank=True, null=True)
    delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    delivery_period_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_period_value = models.IntegerField(blank=True, null=True)
    delivery_product_state_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    order_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                    null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    regular_delivery_price = models.DecimalField(max_digits=14, decimal_places=2,
                                                 blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    set_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    upper_delivery_product_no = models.ForeignKey('self', models.DO_NOTHING,
                                                  db_column='upper_delivery_product_no',
                                                  blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'oms_regulardeliveryproduct'
        unique_together = (('delivery_product_no', 'regular_delivery'),)


class Regulardeliveryschedule(models.Model):
    delivery_product_no = models.OneToOneField(Regulardeliveryproduct,
                                               models.DO_NOTHING,
                                               db_column='delivery_product_no',
                                               primary_key=True)
    regular_delivery_id = models.CharField(max_length=100)
    regular_delivery_order = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_dt = models.DateTimeField(blank=True, null=True)
    delivery_schedule_state_cd = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    regular_delivery_dt = models.DateTimeField()
    ship_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_regulardeliveryschedule'
        unique_together = (
        ('delivery_product_no', 'regular_delivery_id', 'regular_delivery_order'),)


class Uploadconf(models.Model):
    site_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    currency_id = models.CharField(max_length=100, blank=True, null=True)
    currency_price = models.CharField(max_length=50, blank=True, null=True)
    data_row = models.IntegerField(blank=True, null=True)
    local_delivery = models.CharField(max_length=50, blank=True, null=True)
    lp_no = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    order_qty = models.CharField(max_length=50, blank=True, null=True)
    phone1 = models.CharField(max_length=50, blank=True, null=True)
    phone2 = models.CharField(max_length=50, blank=True, null=True)
    sale_price = models.CharField(max_length=50, blank=True, null=True)
    saleproduct_id1 = models.CharField(max_length=50, blank=True, null=True)
    saleproduct_id2 = models.CharField(max_length=50, blank=True, null=True)
    saleproduct_id3 = models.CharField(max_length=50, blank=True, null=True)
    saleproduct_id4 = models.CharField(max_length=50, blank=True, null=True)
    saleproduct_id5 = models.CharField(max_length=50, blank=True, null=True)
    site_order_id = models.CharField(max_length=100, blank=True, null=True)
    title_row = models.IntegerField(blank=True, null=True)
    zip_cd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_uploadconf'
