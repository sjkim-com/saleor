from django.db import models


# Create your models here.

class Catalog(models.Model):
    catalog_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.CharField(max_length=100, blank=True, null=True)
    catalog_type_cd = models.CharField(max_length=100, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    season_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)


class Catalogimg(models.Model):
    catalog_img_no = models.IntegerField()
    catalog_no = models.IntegerField(blank=True, null=True)
    # TODO Origin Foreign Key
    # catalog_no = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='catalog_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    html1 = models.TextField(blank=True, null=True)
    html2 = models.TextField(blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('catalog_img_no', 'catalog_no'),)


class Catalogproduct(models.Model):
    catalog_img_no = models.IntegerField()
    # TODO Unique Foreign Key
    # catalog_img_no = models.ForeignKey(Catalogimg, models.DO_NOTHING,
    #                                       db_column='catalog_img_no', to_field='catalog_img_no')
    catalog_no = models.IntegerField()
    product = models.ForeignKey('pms.Product', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('catalog_img_no', 'catalog_no', 'product'),)


class Display(models.Model):
    display_id = models.CharField(max_length=100, primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_item_type_cd = models.CharField(max_length=100, blank=True, null=True)
    display_type_cd = models.CharField(max_length=100, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    leaf_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    upper_display_id = models.CharField(max_length=100, blank=True, null=True)
    # TODO Self Foreign Key
    # upper_display = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True,
    #                                   related_name='+')
    use_yn = models.CharField(max_length=1, blank=True, null=True)



class Displaycategory(models.Model):
    display_category_id = models.CharField(max_length=100, primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    leaf_yn = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    template = models.ForeignKey('Template', models.DO_NOTHING, blank=True, null=True)
    upper_display_category_id = models.CharField(max_length=100, blank=True, null=True)
    # TODO Self Foreign Key
    # upper_display_category = models.ForeignKey('self', models.DO_NOTHING, blank=True,
    #                                            null=True, related_name='+')



class Displaycategorylang(models.Model):
    display_category = models.ForeignKey(Displaycategory, models.DO_NOTHING
                                            )
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('display_category', 'lang_id'),)


class Displaycategoryproduct(models.Model):
    display_category = models.ForeignKey(Displaycategory, models.DO_NOTHING
                                            )
    product = models.ForeignKey('pms.Product', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('display_category', 'product'),)


class Displayitem(models.Model):
    display = models.ForeignKey(Display, models.DO_NOTHING)
    display_item_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_value = models.CharField(max_length=100, blank=True, null=True)
    control_no = models.IntegerField(blank=True, null=True)
    display_item_div_id = models.CharField(max_length=100, blank=True, null=True)
    display_item_id = models.CharField(max_length=100, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField()
    html1 = models.CharField(max_length=4000, blank=True, null=True)
    html2 = models.CharField(max_length=4000, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    start_dt = models.DateTimeField()
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url1 = models.CharField(max_length=1000, blank=True, null=True)
    url2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('display', 'display_item_no'),)


class Displayitemlang(models.Model):
    display = models.ForeignKey(Displayitem, models.DO_NOTHING)
    display_item_no = models.IntegerField()
    lang_id = models.CharField(max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    html1 = models.CharField(max_length=4000, blank=True, null=True)
    html2 = models.CharField(max_length=4000, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('display', 'display_item_no', 'lang_id'),)


class Exhibit(models.Model):
    exhibit_no = models.AutoField(primary_key=True)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    add_value = models.CharField(max_length=100, blank=True, null=True)
    control_no = models.IntegerField(blank=True, null=True)
    days_week = models.CharField(max_length=100, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)
    exhibit_state_cd = models.CharField(max_length=100, blank=True, null=True)
    exhibit_type_cd = models.CharField(max_length=100, blank=True, null=True)
    html1 = models.CharField(max_length=4000, blank=True, null=True)
    html2 = models.CharField(max_length=4000, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    start_dt = models.DateTimeField(blank=True, null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    sub_html1 = models.CharField(max_length=4000, blank=True, null=True)
    sub_html2 = models.CharField(max_length=4000, blank=True, null=True)
    subtitle = models.CharField(max_length=1000, blank=True, null=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)



class Exhibitbrand(models.Model):
    brand = models.ForeignKey('pms.Brand', models.DO_NOTHING)
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='exhibit_no', to_field='exhibit_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('brand', 'exhibit_no'),)


class Exhibitcoupon(models.Model):
    coupon_no = models.IntegerField()
    # TODO Foreign Key
    # coupon_no = models.OneToOneField('sps.Coupon', models.DO_NOTHING, db_column='coupon_no',
    #                                  primary_key=True)
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='exhibit_no', to_field='exhibit_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('coupon_no', 'exhibit_no'),)


class Exhibitdisplaycategory(models.Model):
    display_category = models.ForeignKey(Displaycategory, models.DO_NOTHING
                                            )
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='exhibit_no', to_field='exhibit_no')
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('display_category', 'exhibit_no'),)


class Exhibitgroup(models.Model):
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING,
                                      db_column='exhibit_no', to_field='exhibit_no')
    group_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    group_type_cd = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    product_display_type1_cd = models.CharField(max_length=100, blank=True, null=True)
    product_display_type2_cd = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    url1 = models.CharField(max_length=1000, blank=True, null=True)
    url2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = (('exhibit_no', 'group_no'),)


class Exhibitlang(models.Model):
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING,
                                      db_column='exhibit_no', to_field='exhibit_no')
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
        unique_together = (('exhibit_no', 'lang_id'),)


class Exhibitoffshop(models.Model):
    exhibit_no = models.ForeignKey(Exhibit, models.DO_NOTHING,
                                      db_column='exhibit_no',to_field='exhibit_no')
    offshop_no = models.IntegerField()
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('exhibit_no', 'offshop_no'),)


class Exhibitproduct(models.Model):
    exhibit_no = models.IntegerField()
    # TODO Unique Foreign Key
    # exhibit_no = models.ForeignKey(Exhibitgroup, models.DO_NOTHING,
    #                                   db_column='exhibit_no',to_field='exhibit_no')
    group_no = models.IntegerField()
    product = models.ForeignKey('pms.Product', models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    display_yn = models.CharField(max_length=1, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)

    class Meta:
        unique_together = (('exhibit_no', 'group_no', 'product'),)


class Template(models.Model):
    template_id = models.CharField(primary_key=True, max_length=100)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sort_no = models.DecimalField(max_digits=14, decimal_places=8, blank=True,
                                  null=True)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    template_type_cd = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    use_yn = models.CharField(max_length=1, blank=True, null=True)



class TemplateDisplay(models.Model):
    display = models.ForeignKey(Display, models.DO_NOTHING)
    template = models.ForeignKey(Template, models.DO_NOTHING)
    ins_dt = models.DateTimeField(blank=True, null=True)
    ins_id = models.CharField(max_length=255, blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    upd_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('display', 'template'),)
