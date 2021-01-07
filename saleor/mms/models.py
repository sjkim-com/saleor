from django.db import models

# Create your models here.
from ..dms.models import Displaycategory


class Address(models.Model):
    address_no = models.AutoField(primary_key=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    delivery_name1 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name2 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name3 = models.CharField(max_length=100, blank=True, null=True)
    delivery_name4 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    phone3 = models.CharField(max_length=100, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_address'
        unique_together = (('address_no', 'member_no'),)


class Blacklist(models.Model):
    blacklist_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    blacklist_reason = models.CharField(max_length=1000, blank=True, null=True)
    blacklist_state_cd = models.CharField(max_length=100, blank=True, null=True)
    blacklist_type_cd = models.CharField(max_length=100, blank=True, null=True)
    end_dt = models.DateTimeField()
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    start_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mms_blacklist'


class Deposit(models.Model):
    deposit_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    claim_no = models.IntegerField(blank=True, null=True)
    deposit_amt = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                      null=True)
    deposit_type_cd = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_deposit'


class Device(models.Model):
    device_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    app_version = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    mobile_os_type_cd = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    push_token = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_device'


class Devicehistory(models.Model):
    device_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    app_version = models.CharField(max_length=100, blank=True, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    mobile_os_type_cd = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    push_token = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_devicehistory'


class Interest(models.Model):
    interest_no = models.AutoField(primary_key=True)
    member_no = models.ForeignKey('mms.Member', models.DO_NOTHING, db_column='member_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('pms.Brand', models.DO_NOTHING, blank=True, null=True)
    display_category = models.ForeignKey(Displaycategory, models.DO_NOTHING, blank=True,
                                         null=True)
    interest_product_type_cd = models.CharField(max_length=100, blank=True, null=True)
    interest_type_cd = models.CharField(max_length=100, blank=True, null=True)
    purpose_type_cd = models.CharField(max_length=100, blank=True, null=True)
    style_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_interest'
        unique_together = (('interest_no', 'member_no'),)


class Interestoffshop(models.Model):
    member_no = models.OneToOneField('Member', models.DO_NOTHING, db_column='member_no',
                                     primary_key=True)
    offshop_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    top_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_interestoffshop'
        unique_together = (('member_no', 'offshop_no'),)


class Loginhistory(models.Model):
    login_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    app_version = models.CharField(max_length=100, blank=True, null=True)
    device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    mobile_os_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_loginhistory'


class Member(models.Model):
    member_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    account_auth_dt = models.DateTimeField(blank=True, null=True)
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    account_no = models.CharField(max_length=100, blank=True, null=True)
    address_no = models.ForeignKey(Address, models.DO_NOTHING, db_column='address_no',
                                   blank=True, null=True)
    app_push_yn = models.CharField(max_length=1, blank=True, null=True)
    bank_cd = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    billing_key = models.CharField(max_length=1000, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    business_no = models.CharField(max_length=100, blank=True, null=True)
    cert_div_cd = models.CharField(max_length=100, blank=True, null=True)
    ciscrhash = models.CharField(max_length=88, blank=True, null=True)
    civersion = models.CharField(max_length=1, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    customer_no = models.CharField(max_length=20, blank=True, null=True)
    discrhash = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    email_yn = models.CharField(max_length=1, blank=True, null=True)
    employee_email = models.CharField(max_length=100, blank=True, null=True)
    employee_reg_dt = models.DateTimeField(blank=True, null=True)
    foreigner_yn = models.CharField(max_length=1, blank=True, null=True)
    gender_cd = models.CharField(max_length=100, blank=True, null=True)
    info_agree_yn = models.CharField(max_length=1, blank=True, null=True)
    member_grade_cd = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_name = models.CharField(max_length=45, blank=True, null=True)
    member_state_cd = models.CharField(max_length=100, blank=True, null=True)
    member_type_cd = models.CharField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=64, blank=True, null=True)
    payment_business_cd = models.CharField(max_length=100, blank=True, null=True)
    payment_method_cd = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    pwd = models.CharField(max_length=1000, blank=True, null=True)
    reg_channel_cd = models.CharField(max_length=100, blank=True, null=True)
    reg_channel_url = models.CharField(max_length=1000, blank=True, null=True)
    reg_device_type_cd = models.CharField(max_length=100, blank=True, null=True)
    regular_payment_business_cd = models.CharField(max_length=100, blank=True,
                                                   null=True)
    regular_payment_business_nm = models.CharField(max_length=100, blank=True,
                                                   null=True)
    regular_payment_device_type_cd = models.CharField(max_length=100, blank=True,
                                                      null=True)
    service_agree_yn = models.CharField(max_length=1, blank=True, null=True)
    sms_yn = models.CharField(max_length=1, blank=True, null=True)
    sns_channel_cd = models.CharField(max_length=100, blank=True, null=True)
    sns_id = models.CharField(max_length=100, blank=True, null=True)
    sns_member_yn = models.CharField(max_length=1, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_member'


class Memberhistory(models.Model):
    member_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    member_grade_cd = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_memberhistory'


class Membermenu(models.Model):
    member_no = models.OneToOneField(Member, models.DO_NOTHING, db_column='member_no',
                                     primary_key=True)
    menu = models.ForeignKey('Quickmenu', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'mms_membermenu'
        unique_together = (('member_no', 'menu'),)


class Password(models.Model):
    member_no = models.OneToOneField(Member, models.DO_NOTHING, db_column='member_no',
                                     primary_key=True)
    password_token = models.CharField(max_length=1000)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    apply_yn = models.CharField(max_length=1, blank=True, null=True)
    expire_dt = models.DateTimeField()
    send_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_password'
        unique_together = (('member_no', 'password_token'),)


class Point(models.Model):
    point_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                  null=True)
    expire_dt = models.DateTimeField()
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    point = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    point_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_point'


class Quickmenu(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    default_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    quickmenu_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_quickmenu'


class Readhistory(models.Model):
    readhistory_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_readhistory'


class Style(models.Model):
    style_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.CharField(max_length=100, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    gender_type_cd = models.CharField(max_length=100, blank=True, null=True)
    like_cnt = models.IntegerField(blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    style_img = models.CharField(max_length=100, blank=True, null=True)
    style_info = models.TextField(blank=True, null=True)
    style_state_cd = models.CharField(max_length=100, blank=True, null=True)
    style_theme_cd = models.CharField(max_length=100, blank=True, null=True)
    theme_cd = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_style'


class Stylelike(models.Model):
    member_no = models.OneToOneField(Member, models.DO_NOTHING, db_column='member_no',
                                     primary_key=True)
    style_no = models.ForeignKey(Style, models.DO_NOTHING, db_column='style_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_stylelike'
        unique_together = (('member_no', 'style_no'),)


class Styleproduct(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    style_no = models.ForeignKey(Style, models.DO_NOTHING, db_column='style_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_styleproduct'
        unique_together = (('product_id', 'style_no'),)


class Wishlist(models.Model):
    wishlist_no = models.OneToOneField('self', models.DO_NOTHING,
                                       db_column='wishlist_no', primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    member_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_no',
                                  blank=True, null=True)
    # product = models.ForeignKey('pms.Product', models.DO_NOTHING, blank=True, null=True)
    # saleproduct = models.ForeignKey('pms.Saleproduct', models.DO_NOTHING, blank=True,
    #                                 null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    upper_wishlist_no = models.ForeignKey('self', models.DO_NOTHING,
                                          db_column='upper_wishlist_no', blank=True,
                                          null=True, related_name='+')
    wishlist_product_type_cd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_wishlist'
