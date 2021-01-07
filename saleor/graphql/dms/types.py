import graphene

from ... import graphql
from ...dms.models import Display, Displaycategory, Displaycategorylang, \
    Displaycategoryproduct
from ...graphql.core.connection import CountableDjangoObjectType
from ...pms.models import *


class DisplayType(CountableDjangoObjectType):
    class Meta:
        model = Display
        fields = ('display_id',
                  'ins_dt',
                  'ins_id',
                  'upd_dt',
                  'upd_id',
                  'display_item_type_cd',
                  'display_type_cd',
                  'display_yn',
                  'leaf_yn',
                  'name',
                  'sort_no',
                  'store_id',
                  'upper_display_id',
                  'use_yn')

    display_id = graphene.String()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    display_item_type_cd = graphene.String()
    display_type_cd = graphene.String()
    display_yn = graphene.String()
    leaf_yn = graphene.String()
    name = graphene.String()
    sort_no = graphene.Decimal()
    store_id = graphene.String()
    upper_display_id = graphene.String()
    use_yn = graphene.String()


class DisplayCategoryType(CountableDjangoObjectType):
    class Meta:
        model = Displaycategory
        fields = ('display_category_id',
                  'ins_dt',
                  'ins_id',
                  'upd_dt',
                  'upd_id',
                  'display_yn',
                  'leaf_yn',
                  'name',
                  'note',
                  'sort_no',
                  'store_id',
                  'upper_display_category_id',
                  'template_id')

    display_category_id = graphene.String()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    display_yn = graphene.String()
    leaf_yn = graphene.String()
    name = graphene.String()
    note = graphene.String()
    sort_no = graphene.Decimal()
    store_id = graphene.String()
    upper_display_category_id = graphene.String()
    template_id = graphene.String()


class DisplayCategoryLangType(CountableDjangoObjectType):
    class Meta:
        model = Displaycategorylang
        fields = ('id',
                  'lang_id',
                  'ins_dt',
                  'ins_id',
                  'upd_dt',
                  'upd_id',
                  'name',
                  'note',
                  'display_category_id')

    id = graphene.Int()
    lang_id = graphene.String()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    name = graphene.String()
    note = graphene.String()
    display_category_id = graphene.String()


class DisplayCategoryProductType(CountableDjangoObjectType):
    class Meta:
        model = Displaycategoryproduct
        fields = ('id',
                  'ins_dt',
                  'ins_id',
                  'upd_dt',
                  'upd_id',
                  'display_yn',
                  'sort_no',
                  'display_category_id',
                  'product_id',)

    id = graphene.Int()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    display_yn = graphene.String()
    sort_no = graphene.Decimal()
    display_category_id = graphene.String()
    product_id = graphene.String()
