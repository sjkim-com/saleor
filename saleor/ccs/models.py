from django.db import models


# Create your models here.

class Accessfunction(models.Model):
    function = models.ForeignKey('Function', models.DO_NOTHING)
    menu = models.ForeignKey('Accessmenu', models.DO_NOTHING)
    role_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('function', 'menu', 'role_no'),)


class Accessmenu(models.Model):
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    role_no = models.ForeignKey('Role', models.DO_NOTHING, to_field="role_no",db_column='role_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('menu', 'role_no'),)


class Affiliatedbinout(models.Model):
    business_no = models.IntegerField()
    io_div = models.CharField(max_length=1)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    api_client_id = models.CharField(max_length=100, blank=True, null=True)
    api_client_key = models.CharField(max_length=20, blank=True, null=True)
    io_user_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('business_no', 'io_div'),)


class Apply(models.Model):
    apply_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    target_type_cd = models.CharField(max_length=100, blank=True, null=True)


class Applytarget(models.Model):
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, to_field="apply_no",db_column='apply_no'
                                    )
    target_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('apply_no', 'target_id'),)


class Batchlog(models.Model):
    batch_id = models.CharField(max_length=100)
    batch_log_no = models.IntegerField(blank=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=4000, blank=True, null=True)
    start_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (('batch_id', 'batch_log_no'),)


class Business(models.Model):
    business_no = models.IntegerField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    business_condition = models.CharField(max_length=100, blank=True, null=True)
    business_state_cd = models.CharField(max_length=100, blank=True, null=True)
    business_tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    business_type = models.CharField(max_length=200, blank=True, null=True)
    business_type_cd = models.CharField(max_length=100, blank=True, null=True)
    contract_end_dt = models.DateTimeField(blank=True, null=True)
    contract_start_dt = models.DateTimeField(blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    depositor_name = models.CharField(max_length=100, blank=True, null=True)
    erp_business_id = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    manager_email = models.CharField(max_length=100, blank=True, null=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    manager_phone1 = models.CharField(max_length=100, blank=True, null=True)
    manager_phone2 = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    overseas_purchase_yn = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=100, blank=True, null=True)
    rep_name = models.CharField(max_length=200, blank=True, null=True)
    req_user_id = models.CharField(max_length=100, blank=True, null=True)
    req_user_pwd = models.CharField(max_length=1000, blank=True, null=True)
    sale_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sales_email = models.CharField(max_length=100, blank=True, null=True)
    sales_name = models.CharField(max_length=100, blank=True, null=True)
    sales_phone1 = models.CharField(max_length=100, blank=True, null=True)
    sales_phone2 = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    supply_item = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)
    sf_id = models.CharField(max_length=100, blank=True, null=True)


class Businessholiday(models.Model):
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                       db_column='business_no')
    holiday = models.CharField(max_length=8)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('business_no', 'holiday'),)


class Businessinquiry(models.Model):
    business_inquiry_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    dep_name = models.CharField(max_length=200, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    homepage_url = models.CharField(max_length=200, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    manager_email = models.CharField(max_length=100, blank=True, null=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    manager_phone1 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)


class Businessinquirycategory(models.Model):
    business_inquiry_no = models.ForeignKey(Businessinquiry, models.DO_NOTHING,to_field="business_inquiry_no",
                                               db_column='business_inquiry_no'
                                               )
    category_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('business_inquiry_no', 'category_id'),)


class Businesspolicy(models.Model):
    policy = models.ForeignKey('Policy', models.DO_NOTHING)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    storepolicy_id = models.IntegerField()

    class Meta:
        unique_together = (('policy', 'business_no', 'store', 'storepolicy_id'),)


class Channel(models.Model):
    channel_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    business_channel_id = models.CharField(max_length=100, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no', blank=True, null=True)
    channel_state_cd = models.CharField(max_length=100, blank=True, null=True)
    channel_type_cd = models.CharField(max_length=100, blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)
    mobile_url = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    pc_url = models.CharField(max_length=1000, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)


class Code(models.Model):
    cd = models.CharField(max_length=100)
    cd_group_cd = models.ForeignKey('Codegroup', models.DO_NOTHING,to_field="cd_group_cd",
                                    db_column='cd_group_cd')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('cd', 'cd_group_cd'),)


class Codegroup(models.Model):
    cd_group_cd = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    cd_group_type_cd = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)


class Codegrouplang(models.Model):
    cd_group_cd = models.ForeignKey(Codegroup, models.DO_NOTHING,to_field="cd_group_cd",
                                       db_column='cd_group_cd')
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('cd_group_cd', 'lang_id'),)


class Codelang(models.Model):
    cd_fk = models.ForeignObject(Code, from_fields=['cd', 'cd_group_cd'],to_fields=['cd', 'cd_group_cd'],on_delete=models.CASCADE)
    # cd = models.ForeignKey(Code, models.DO_NOTHING, to_field="cd",db_column='cd')
    cd = models.CharField(max_length=100)
    cd_group_cd = models.CharField(max_length=100)
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('cd', 'cd_group_cd', 'lang_id'),)


class Commission(models.Model):
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                       db_column='business_no')
    commission_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    # category = models.ForeignKey('pms.Category', models.DO_NOTHING, blank=True,
    #                              null=True)
    commission_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                          null=True)

    class Meta:
        unique_together = (('business_no', 'commission_no'),)


class Control(models.Model):
    control_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    channel_control_cd = models.CharField(max_length=100, blank=True, null=True)


class Controlchannel(models.Model):
    channel_no = models.ForeignKey(Channel, models.DO_NOTHING, to_field="channel_no",
                                      db_column='channel_no')
    control_no = models.ForeignKey(Control, models.DO_NOTHING, to_field="control_no",db_column='control_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('channel_no', 'control_no'),)


class Controldevice(models.Model):
    control_no = models.ForeignKey(Control, models.DO_NOTHING,to_field="control_no",
                                      db_column='control_no')
    device_type_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('control_no', 'device_type_cd'),)


class Controlmembergrade(models.Model):
    control_no = models.ForeignKey(Control, models.DO_NOTHING,to_field="control_no",
                                      db_column='control_no')
    member_grade_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('control_no', 'member_grade_cd'),)


class Controlmembertype(models.Model):
    control_no = models.ForeignKey(Control, models.DO_NOTHING,to_field="control_no",
                                      db_column='control_no')
    member_type_cd = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('control_no', 'member_type_cd'),)


class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    currency_id = models.CharField(max_length=100, blank=True, null=True)
    currency_unit = models.CharField(max_length=20, blank=True, null=True)
    currency_unit_prefix_yn = models.CharField(max_length=1, blank=True, null=True)
    date_format = models.CharField(max_length=100, blank=True, null=True)
    datetime_format = models.CharField(max_length=100, blank=True, null=True)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    lang_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)


class Currency(models.Model):
    currency_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    exchange_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                        null=True)
    name = models.CharField(max_length=100, blank=True, null=True)


class Deliveryfee(models.Model):
    delivery_policy_no = models.ForeignKey('Deliverypolicy', models.DO_NOTHING,to_field="delivery_policy_no",
                                              db_column='delivery_policy_no'
                                              )
    zip_cd = models.CharField(max_length=20)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    delivery_yn = models.CharField(max_length=1, blank=True, null=True)
    min_delivery_free_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)

    class Meta:
        unique_together = (('delivery_policy_no', 'zip_cd'),)


class Deliverypolicy(models.Model):
    delivery_policy_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no', blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                       null=True)
    delivery_fee_type_cd = models.CharField(max_length=100, blank=True, null=True)
    delivery_info = models.CharField(max_length=1000, blank=True, null=True)
    delivery_service_cd = models.CharField(max_length=100, blank=True, null=True)
    exchange_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    min_delivery_free_amt = models.DecimalField(max_digits=14, decimal_places=2,
                                                blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    return_delivery_fee = models.DecimalField(max_digits=14, decimal_places=2,
                                              blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)
    tax_type_cd = models.CharField(max_length=100, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True,
                                   null=True)


class Excproduct(models.Model):
    apply_no = models.ForeignKey(Apply, models.DO_NOTHING, to_field="apply_no",db_column='apply_no'
                                    )
    product = models.ForeignKey('pms.Product', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('apply_no', 'product'),)


class Faq(models.Model):
    faq_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    faq_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)


class Faqlang(models.Model):
    faq_no = models.ForeignKey(Faq, models.DO_NOTHING, to_field="faq_no",db_column='faq_no'
                                  )
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('faq_no', 'lang_id'),)


class Function(models.Model):
    function_id = models.CharField(max_length=100)
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = (('function_id', 'menu'),)


class Functionlang(models.Model):
    function = models.ForeignKey(Function, models.DO_NOTHING)
    lang_id = models.CharField(max_length=100)
    menu_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('function', 'lang_id', 'menu_id'),)


class Functionurl(models.Model):
    function = models.ForeignKey(Function, models.DO_NOTHING)
    menu_id = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('function', 'menu_id', 'url'),)


class Inquiry(models.Model):
    inquiry_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answer_dt = models.DateTimeField(blank=True, null=True)
    answer_id = models.CharField(max_length=100, blank=True, null=True)
    brand_id = models.CharField(max_length=100, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no', blank=True, null=True)
    confirm_dt = models.DateTimeField(blank=True, null=True)
    confirm_id = models.CharField(max_length=100, blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email_yn = models.CharField(max_length=1, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    inquiry_channel_cd = models.CharField(max_length=100, blank=True, null=True)
    inquiry_state_cd = models.CharField(max_length=100, blank=True, null=True)
    inquiry_type_cd = models.CharField(max_length=100, blank=True, null=True)
    member_no = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    saleproduct_id = models.CharField(max_length=100, blank=True, null=True)
    sms_yn = models.CharField(max_length=1, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)


class Inquirytransfer(models.Model):
    inquiry_transfer_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    inquiry_no = models.ForeignKey(Inquiry, models.DO_NOTHING, to_field="inquiry_no",db_column='inquiry_no',
                                   blank=True, null=True)
    transfer_note = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)


class Language(models.Model):
    lang_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)


class Menu(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    menu_group = models.ForeignKey('Menugroup', models.DO_NOTHING, blank=True,
                                   null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    system_type_cd = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)


class Menugroup(models.Model):
    menu_group_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)


class Menugrouplang(models.Model):
    lang_id = models.CharField(max_length=100)
    menu_group = models.ForeignKey(Menugroup, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'menu_group'),)


class Menulang(models.Model):
    lang_id = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'menu'),)


class Messagelog(models.Model):
    message_log_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_send_state_cd = models.CharField(max_length=100, blank=True, null=True)
    message_type_cd = models.CharField(max_length=100, blank=True, null=True)
    reserve_dt = models.DateTimeField(blank=True, null=True)
    send_dt = models.DateTimeField(blank=True, null=True)
    send_error_reason = models.CharField(max_length=1000, blank=True, null=True)
    sender_id = models.CharField(max_length=100, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    target_id = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)


class Mobileauth(models.Model):
    mobile_auth_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    auth_key = models.CharField(max_length=20, blank=True, null=True)
    expire_dt = models.DateTimeField()
    mobile_phone = models.CharField(max_length=64, blank=True, null=True)


class Notice(models.Model):
    notice_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField()
    event_no = models.IntegerField(blank=True, null=True)
    event_target_div_cd = models.CharField(max_length=100, blank=True, null=True)
    notice_type_cd = models.CharField(max_length=100, blank=True, null=True)
    read_cnt = models.IntegerField(blank=True, null=True)
    start_dt = models.DateTimeField()
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    top_notice_yn = models.CharField(max_length=1, blank=True, null=True)


class NoticeBrand(models.Model):
    brand = models.ForeignKey('pms.Brand', models.DO_NOTHING)
    notice_no = models.ForeignKey(Notice, models.DO_NOTHING, to_field="notice_no",db_column='notice_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('brand', 'notice_no'),)


class Noticelang(models.Model):
    lang_id = models.CharField(max_length=100)
    notice_no = models.ForeignKey(Notice, models.DO_NOTHING, to_field="notice_no",db_column='notice_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=4000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'notice_no'),)


class Noticeproduct(models.Model):
    notice_no = models.ForeignKey(Notice, models.DO_NOTHING, to_field="notice_no",db_column='notice_no'
                                     )
    product = models.ForeignKey('pms.Product', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('notice_no', 'product'),)


class Offshop(models.Model):
    offshop_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    address_info = models.CharField(max_length=4000, blank=True, null=True)
    area_div1 = models.CharField(max_length=100, blank=True, null=True)
    area_div2 = models.CharField(max_length=100, blank=True, null=True)
    business_end_time = models.CharField(max_length=6, blank=True, null=True)
    business_hours_info = models.CharField(max_length=200, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no', blank=True, null=True)
    business_start_time = models.CharField(max_length=6, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    holiday_info = models.CharField(max_length=4000, blank=True, null=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                    null=True)
    manager_phone = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    offshop_affiliation = models.CharField(max_length=200, blank=True, null=True)
    offshop_phone = models.CharField(max_length=100, blank=True, null=True)
    offshop_pickup_yn = models.CharField(max_length=1, blank=True, null=True)
    offshop_state_cd = models.CharField(max_length=100, blank=True, null=True)
    offshop_type_cd = models.CharField(max_length=100, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)


class Offshopbrand(models.Model):
    brand = models.ForeignKey('pms.Brand', models.DO_NOTHING)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, to_field="offshop_no",db_column='offshop_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('brand', 'offshop_no'),)


class Offshopholiday(models.Model):
    holiday = models.CharField(max_length=8)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, to_field="offshop_no",db_column='offshop_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('holiday', 'offshop_no'),)


class Offshoplang(models.Model):
    lang_id = models.CharField(max_length=100)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, to_field="offshop_no",db_column='offshop_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'offshop_no'),)


class Policy(models.Model):
    policy_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    policy_type_cd = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)


class Policylang(models.Model):
    lang_id = models.CharField(max_length=100)
    policy = models.ForeignKey(Policy, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'policy'),)


class Popup(models.Model):
    popup_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail1 = models.CharField(max_length=4000, blank=True, null=True)
    detail2 = models.CharField(max_length=4000, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField()
    mobile_display_yn = models.CharField(max_length=1, blank=True, null=True)
    pc_display_yn = models.CharField(max_length=1, blank=True, null=True)
    popup_type_cd = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    start_dt = models.DateTimeField()
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)


class Popupurl(models.Model):
    popup_no = models.ForeignKey(Popup, models.DO_NOTHING, to_field="popup_no",db_column='popup_no'
                                    )
    popup_url_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    device_channel_type_cd = models.CharField(max_length=100, blank=True, null=True)
    popup_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('popup_no', 'popup_url_no'),)


class Role(models.Model):
    role_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    sf_id = models.CharField(max_length=100, blank=True, null=True)


class Site(models.Model):
    site_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    erp_business_id = models.CharField(max_length=100, blank=True, null=True)
    logistics_use_yn = models.CharField(max_length=1, blank=True, null=True)
    mall_id = models.CharField(max_length=100, blank=True, null=True)
    mall_user_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    site_type_cd = models.CharField(max_length=100, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)


class Snsshare(models.Model):
    sns_share_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    img_url = models.CharField(max_length=1000, blank=True, null=True)
    ref_id = models.CharField(max_length=100, blank=True, null=True)
    share_item_cd = models.CharField(max_length=100, blank=True, null=True)
    tag_url = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)


class Store(models.Model):
    store_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    country_no = models.CharField(max_length=20, blank=True, null=True)
    lang_id = models.CharField(max_length=100, blank=True, null=True)
    manager_email = models.CharField(max_length=100, blank=True, null=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    manager_phone = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    store_state_cd = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    zip_cd = models.CharField(max_length=20, blank=True, null=True)


class Storecountry(models.Model):
    country_id = models.CharField(max_length=100)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    currency_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('country_id', 'store'),)


class Storelang(models.Model):
    lang_id = models.CharField(max_length=100)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    address4 = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'store'),)


class Storelanguage(models.Model):
    lang_id = models.CharField(max_length=100)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'store'),)


class Storepolicy(models.Model):
    policy = models.ForeignKey(Policy, models.DO_NOTHING)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    storepolicy_id = models.IntegerField()

    class Meta:
        unique_together = (('policy', 'store', 'storepolicy_id'),)


class Translate(models.Model):
    lang_id = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('lang_id', 'source'),)


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    business_no = models.ForeignKey(Business, models.DO_NOTHING,to_field="business_no",
                                    db_column='business_no', blank=True, null=True)
    current_connect_dt = models.DateTimeField(blank=True, null=True)
    current_connect_ip = models.CharField(max_length=20, blank=True, null=True)
    dep_cd = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    emp_id = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    last_connect_dt = models.DateTimeField(blank=True, null=True)
    last_connect_ip = models.CharField(max_length=20, blank=True, null=True)
    login_fail_cnt = models.IntegerField(blank=True, null=True)
    md_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    offshop_no = models.ForeignKey(Offshop, models.DO_NOTHING, to_field="offshop_no",db_column='offshop_no',
                                   blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    pwd = models.CharField(max_length=1000, blank=True, null=True)
    pwd_init_yn = models.CharField(max_length=1, blank=True, null=True)
    pwd_upd_dt = models.DateTimeField(blank=True, null=True)
    role_no = models.ForeignKey(Role, models.DO_NOTHING, to_field="role_no",db_column='role_no',
                                blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)
    user_state_cd = models.CharField(max_length=100, blank=True, null=True)
    user_type_cd = models.CharField(max_length=100, blank=True, null=True)
    sf_id = models.CharField(max_length=100, blank=True, null=True)


class Userrolehistory(models.Model):
    user_role_history_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_no = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)


class ZipcodeJp(models.Model):
    zip_cd = models.CharField(max_length=7)
    group_code = models.CharField(max_length=20, blank=True, null=True)
    old_zip_cd = models.CharField(max_length=5, blank=True, null=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    address1_kana = models.CharField(max_length=200)
    address2_kana = models.CharField(max_length=200)
    address3_kana = models.CharField(max_length=200)
    flag1 = models.CharField(max_length=1, blank=True, null=True)
    flag2 = models.CharField(max_length=1, blank=True, null=True)
    flag3 = models.CharField(max_length=1, blank=True, null=True)
    flag4 = models.CharField(max_length=1, blank=True, null=True)
    flag5 = models.CharField(max_length=1, blank=True, null=True)
    flag6 = models.CharField(max_length=1, blank=True, null=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=100, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (
            ('zip_cd', 'address1', 'address2', 'address3', 'address3_kana'),)
