from django.db import models

# Create your models here.
from ..ccs.models import Business, Control, Apply
from ..mms.models import Member
from ..pms.models import Brand, Product


class Cardpromotion(models.Model):
    card_promotion_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    card_promotion_state_cd = models.CharField(max_length=100, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    html1 = models.TextField(blank=True, null=True)
    html2 = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_dt = models.DateTimeField(blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_cardpromotion'


class Cardpromotionlang(models.Model):
    card_promotion_no = models.OneToOneField(Cardpromotion, models.DO_NOTHING,
                                             db_column='card_promotion_no',
                                             primary_key=True)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    html1 = models.CharField(max_length=4000, blank=True, null=True)
    html2 = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_cardpromotionlang'
        unique_together = (('card_promotion_no', 'lang_id'),)


class Coupon(models.Model):
    coupon_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    affiliate_yn = models.CharField(max_length=1, blank=True, null=True)
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, db_column='apply_no',
                                 blank=True, null=True)
    business_burden_rate = models.DecimalField(max_digits=14, decimal_places=2,
                                               blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,
                                    db_column='business_no', blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    coupon_issue_type_cd = models.CharField(max_length=100, blank=True, null=True)
    coupon_state_cd = models.CharField(max_length=100, blank=True, null=True)
    coupon_type_cd = models.CharField(max_length=100, blank=True, null=True)
    dc_apply_type_cd = models.CharField(max_length=100, blank=True, null=True)
    dc_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    deal_apply_yn = models.CharField(max_length=1, blank=True, null=True)
    discount_dup_yn = models.CharField(max_length=1, blank=True, null=True)
    down_show_yn = models.CharField(max_length=1, blank=True, null=True)
    issue_end_dt = models.DateTimeField()
    issue_start_dt = models.DateTimeField()
    max_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    max_issue_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                        null=True)
    max_mem_issue_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                            null=True)
    mem_issue_basis_cd = models.CharField(max_length=100, blank=True, null=True)
    min_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    single_apply_yn = models.CharField(max_length=1, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    term_days = models.IntegerField(blank=True, null=True)
    term_end_dt = models.DateTimeField(blank=True, null=True)
    term_start_dt = models.DateTimeField(blank=True, null=True)
    term_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_coupon'


class Coupondeal(models.Model):
    coupon_no = models.OneToOneField(Coupon, models.DO_NOTHING, db_column='coupon_no',
                                     primary_key=True)
    deal_no = models.ForeignKey('Deal', models.DO_NOTHING, db_column='deal_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_coupondeal'
        unique_together = (('coupon_no', 'deal_no'),)


class Couponissue(models.Model):
    coupon_issue_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    coupon_issue_state_cd = models.CharField(max_length=100, blank=True, null=True)
    coupon_no = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='coupon_no',
                                  blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    private_cin = models.CharField(max_length=100, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True)
    use_dt = models.DateTimeField(blank=True, null=True)
    use_end_dt = models.DateTimeField(blank=True, null=True)
    use_start_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_couponissue'


class Couponlang(models.Model):
    coupon_no = models.OneToOneField(Coupon, models.DO_NOTHING, db_column='coupon_no',
                                     primary_key=True)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_couponlang'
        unique_together = (('coupon_no', 'lang_id'),)


class Deal(models.Model):
    deal_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    deal_type_cd = models.CharField(max_length=100, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_deal'


class Dealgroup(models.Model):
    deal_group_no = models.OneToOneField('self', models.DO_NOTHING,
                                         db_column='deal_group_no', primary_key=True)
    deal_no = models.ForeignKey(Deal, models.DO_NOTHING, db_column='deal_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    upper_deal_group_no = models.ForeignKey('self', models.DO_NOTHING,
                                            db_column='upper_deal_group_no', blank=True,
                                            null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'sps_dealgroup'
        unique_together = (('deal_group_no', 'deal_no'),)


class Dealmember(models.Model):
    deal_no = models.OneToOneField('Dealproduct', models.DO_NOTHING,
                                   db_column='deal_no', primary_key=True)
    deal_product_no = models.IntegerField()
    member_grade_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)
    pre_open_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_dealmember'
        unique_together = (('deal_no', 'deal_product_no', 'member_grade_cd'),)


class Dealproduct(models.Model):
    deal_no = models.OneToOneField(Deal, models.DO_NOTHING, db_column='deal_no',
                                   primary_key=True)
    deal_product_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    deal_group_no = models.ForeignKey(Dealgroup, models.DO_NOTHING,
                                      db_column='deal_group_no', blank=True, null=True)
    deal_state_cd = models.CharField(max_length=100, blank=True, null=True)
    deal_stock_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                         null=True)
    delivery_fee_free_yn = models.CharField(max_length=1, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    point_save_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    start_dt = models.DateTimeField(blank=True, null=True)
    supply_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    total_deal_stock_qty = models.DecimalField(max_digits=10, decimal_places=0,
                                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_dealproduct'
        unique_together = (('deal_no', 'deal_product_no'),)


class Dealsaleproductprice(models.Model):
    deal_no = models.OneToOneField(Dealproduct, models.DO_NOTHING, db_column='deal_no',
                                   primary_key=True)
    deal_product_no = models.IntegerField()
    saleproduct_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_sale_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                         null=True)

    class Meta:
        managed = False
        db_table = 'sps_dealsaleproductprice'
        unique_together = (('deal_no', 'deal_product_no', 'saleproduct_id'),)


class Discount(models.Model):
    discount_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, db_column='apply_no',
                                 blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    coupon_show_yn = models.CharField(max_length=1, blank=True, null=True)
    dc_apply_type_cd = models.CharField(max_length=100, blank=True, null=True)
    dc_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)
    discount_state_cd = models.CharField(max_length=100, blank=True, null=True)
    discount_type_cd = models.CharField(max_length=100, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    max_dc_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                     null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_dt = models.DateTimeField(blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_discount'


class Discountlang(models.Model):
    discount_no = models.OneToOneField(Discount, models.DO_NOTHING,
                                       db_column='discount_no', primary_key=True)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_discountlang'
        unique_together = (('discount_no', 'lang_id'),)


class Event(models.Model):
    event_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    event_div_cd = models.CharField(max_length=100, blank=True, null=True)
    event_end_dt = models.DateTimeField()
    event_join_end_dt = models.DateTimeField()
    event_join_start_dt = models.DateTimeField()
    event_start_dt = models.DateTimeField()
    event_state_cd = models.CharField(max_length=100, blank=True, null=True)
    event_type_cd = models.CharField(max_length=100, blank=True, null=True)
    html1 = models.TextField(blank=True, null=True)
    html2 = models.TextField(blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    join_control_cd = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    reply_display_yn = models.CharField(max_length=1, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    win_notice_date = models.DateTimeField()
    winner_show_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_event'


class Eventattend(models.Model):
    event_attend_no = models.AutoField(primary_key=True)
    event_no = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    day_value = models.IntegerField(blank=True, null=True)
    join_end_dt = models.DateTimeField(blank=True, null=True)
    join_start_dt = models.DateTimeField(blank=True, null=True)
    join_type_cd = models.CharField(max_length=100, blank=True, null=True)
    lottery_yn = models.CharField(max_length=1, blank=True, null=True)
    prize_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventattend'
        unique_together = (('event_attend_no', 'event_no'),)


class Eventbrand(models.Model):
    brand = models.OneToOneField(Brand, models.DO_NOTHING, primary_key=True)
    event_no = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventbrand'
        unique_together = (('brand', 'event_no'),)


class Eventcoupon(models.Model):
    coupon_no = models.OneToOneField(Coupon, models.DO_NOTHING, db_column='coupon_no',
                                     primary_key=True)
    event_no = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventcoupon'
        unique_together = (('coupon_no', 'event_no'),)


class Eventjoin(models.Model):
    join_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    event_no = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_no',
                                 blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    prize_no = models.IntegerField(blank=True, null=True)
    win_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventjoin'


class Eventlang(models.Model):
    event_no = models.OneToOneField(Event, models.DO_NOTHING, db_column='event_no',
                                    primary_key=True)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    html1 = models.CharField(max_length=4000, blank=True, null=True)
    html2 = models.CharField(max_length=4000, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventlang'
        unique_together = (('event_no', 'lang_id'),)


class Eventprize(models.Model):
    event_no = models.OneToOneField(Event, models.DO_NOTHING, db_column='event_no',
                                    primary_key=True)
    prize_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    prize = models.CharField(max_length=100, blank=True, null=True)
    prize_type_cd = models.CharField(max_length=100, blank=True, null=True)
    winner_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_eventprize'
        unique_together = (('event_no', 'prize_no'),)


class Pointsave(models.Model):
    point_save_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, db_column='apply_no',
                                 blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    end_dt = models.DateTimeField()
    name = models.CharField(max_length=100, blank=True, null=True)
    point_save_state_cd = models.CharField(max_length=100, blank=True, null=True)
    point_save_type_cd = models.CharField(max_length=100, blank=True, null=True)
    point_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    start_dt = models.DateTimeField()
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_pointsave'


class Pointsavelang(models.Model):
    lang_id = models.CharField(primary_key=True, max_length=100)
    point_save_no = models.ForeignKey(Pointsave, models.DO_NOTHING,
                                      db_column='point_save_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_pointsavelang'
        unique_together = (('lang_id', 'point_save_no'),)


class Present(models.Model):
    present_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, db_column='apply_no',
                                 blank=True, null=True)
    control_no = models.ForeignKey(Control, models.DO_NOTHING, db_column='control_no',
                                   blank=True, null=True)
    deal_apply_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    max_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    min_order_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    present_select_type_cd = models.CharField(max_length=100, blank=True, null=True)
    present_state_cd = models.CharField(max_length=100, blank=True, null=True)
    present_type_cd = models.CharField(max_length=100, blank=True, null=True)
    select_qty = models.DecimalField(max_digits=10, decimal_places=0, blank=True,
                                     null=True)
    start_dt = models.DateTimeField(blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,
                                    db_column='business_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_present'


class Presentdeal(models.Model):
    deal_no = models.OneToOneField(Deal, models.DO_NOTHING, db_column='deal_no',
                                   primary_key=True)
    present_no = models.ForeignKey(Present, models.DO_NOTHING, db_column='present_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_presentdeal'
        unique_together = (('deal_no', 'present_no'),)


class Presentlang(models.Model):
    lang_id = models.CharField(primary_key=True, max_length=100)
    present_no = models.ForeignKey(Present, models.DO_NOTHING, db_column='present_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_presentlang'
        unique_together = (('lang_id', 'present_no'),)


class Presentproduct(models.Model):
    present_no = models.OneToOneField(Present, models.DO_NOTHING,
                                      db_column='present_no', primary_key=True)
    product_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_presentproduct'
        unique_together = (('present_no', 'product_id'),)
