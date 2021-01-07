from django.db.models import Q

from ...dms import models


# テーブルの全データを取得
def resolve_display(info):
    qs = models.Display.objects.all()
    return qs


# テーブルのデータでIDから取得
def resolve_display_id(id):
    qs = models.Display.objects.get(pk=id)
    return qs


def resolve_display_search(info):
    qs = models.Display.objects.filter(
        Q(display_id=info['display_id']) |
        Q(ins_dt=info['ins_dt']) |
        Q(ins_id=info['ins_id']) |
        Q(upd_dt=info['upd_dt']) |
        Q(upd_id=info['upd_id']) |
        Q(display_item_type_cd=info['display_item_type_cd']) |
        Q(display_type_cd=info['display_type_cd']) |
        Q(display_yn=info['display_yn']) |
        Q(leaf_yn=info['leaf_yn']) |
        Q(name=info['name']) |
        Q(sort_no=info['sort_no']) |
        Q(store_id=info['store_id']) |
        Q(upper_display_id=info['upper_display_id']) |
        Q(use_yn=info['use_yn'])
    )
    return qs


# テーブルの全データを取得
def resolve_displaycategory(info):
    qs = models.Displaycategory.objects.all()
    return qs


# テーブルのデータでIDから取得
def resolve_displaycategory_id(id):
    qs = models.Displaycategory.objects.get(pk=id)
    return qs


def resolve_displaycategory_search(info):
    qs = models.Displaycategory.objects.filter(
        Q(display_category_id=info['display_category_id']) |
        Q(ins_dt=info['ins_dt']) |
        Q(ins_id=info['ins_id']) |
        Q(upd_dt=info['upd_dt']) |
        Q(upd_id=info['upd_id']) |
        Q(display_yn=info['display_yn']) |
        Q(leaf_yn=info['leaf_yn']) |
        Q(name=info['name']) |
        Q(note=info['note']) |
        Q(sort_no=info['sort_no']) |
        Q(store_id=info['store_id']) |
        Q(upper_display_category_id=info['upper_display_category_id']) |
        Q(template_id=info['template_id'])
    )
    return qs


# テーブルの全データを取得
def resolve_displaycategorylang(info):
    qs = models.Displaycategorylang.objects.all()
    return qs


# テーブルのデータでIDから取得
def resolve_displaycategorylang_id(id):
    qs = models.Displaycategorylang.objects.get(pk=id)
    return qs


def resolve_displaycategorylang_lang(data):
    qs = models.Displaycategorylang.objects.filter(
        display_category_id=data['display_category_id'], lang_id=data['lang_id'])
    return qs


def resolve_displaycategorylang_search(info):
    qs = models.Displaycategorylang.objects.filter(
        Q(id=info['id']) |
        Q(lang_id=info['lang_id']) |
        Q(ins_dt=info['ins_dt']) |
        Q(ins_id=info['ins_id']) |
        Q(upd_dt=info['upd_dt']) |
        Q(upd_id=info['upd_id']) |
        Q(name=info['name']) |
        Q(note=info['note']) |
        Q(display_category_id=info['display_category_id'])
    )
    return qs


# テーブルの全データを取得
def resolve_displaycategoryproduct(info):
    qs = models.Displaycategoryproduct.objects.all()
    return qs


# テーブルのデータでIDから取得
def resolve_displaycategoryproduct_id(id):
    qs = models.Displaycategoryproduct.objects.get(pk=id)
    return qs


def resolve_displaycategoryproduct_product(id):
    qs = models.Displaycategoryproduct.objects.filter(product_id=id)
    return qs


def resolve_displaycategoryproduct_search(info):
    qs = models.Displaycategoryproduct.objects.filter(
        Q(id=info['id']) |
        Q(ins_dt=info['ins_dt']) |
        Q(ins_id=info['ins_id']) |
        Q(upd_dt=info['upd_dt']) |
        Q(upd_id=info['upd_id']) |
        Q(display_yn=info['display_yn']) |
        Q(sort_no=info['sort_no']) |
        Q(display_category_id=info['display_category_id']) |
        Q(product_id=info['product_id'])
    )
    return qs
