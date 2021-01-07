import graphene

from .resolver import resolve_display, resolve_display_id, resolve_display_search, \
    resolve_displaycategory, resolve_displaycategory_id, resolve_displaycategory_search, \
    resolve_displaycategorylang, resolve_displaycategorylang_id, \
    resolve_displaycategorylang_lang, resolve_displaycategorylang_search, \
    resolve_displaycategoryproduct, resolve_displaycategoryproduct_id, \
    resolve_displaycategoryproduct_product, resolve_displaycategoryproduct_search
from .types import DisplayType, DisplayCategoryType, DisplayCategoryLangType, \
    DisplayCategoryProductType
from ...graphql.pms.types import Category
from ...dms import models


class DmsQueries(graphene.ObjectType):
    display = graphene.List(
        DisplayType
    )

    display_id = graphene.Field(DisplayType, id=graphene.String())

    display_search = graphene.List(
        DisplayType,
        display_id=graphene.Argument(graphene.ID, description="Test"),
        ins_dt=graphene.Argument(graphene.Date, description="Test"),
        ins_id=graphene.Argument(graphene.String, description="Test"),
        upd_dt=graphene.Argument(graphene.Date, description="Test"),
        upd_id=graphene.Argument(graphene.String, description="Test"),
        display_item_type_cd=graphene.Argument(graphene.String, description="Test"),
        display_type_cd=graphene.Argument(graphene.String, description="Test"),
        display_yn=graphene.Argument(graphene.String, description="Test"),
        leaf_yn=graphene.Argument(graphene.String, description="Test"),
        name=graphene.Argument(graphene.String, description="Test"),
        sort_no=graphene.Argument(graphene.Decimal, description="Test"),
        store_id=graphene.Argument(graphene.String, description="Test"),
        upper_display_id=graphene.Argument(graphene.String, description="Test"),
        use_yn=graphene.Argument(graphene.String, description="Test"),
        description="Look up DMS Display",
    )

    displaycategory = graphene.List(
        DisplayCategoryType
    )

    displaycategory_id = graphene.Field(DisplayCategoryType, id=graphene.String())

    displaycategory_search = graphene.List(
        DisplayCategoryType,
        display_category_id=graphene.Argument(graphene.ID, description="Test"),
        ins_dt=graphene.Argument(graphene.Date, description="Test"),
        ins_id=graphene.Argument(graphene.String, description="Test"),
        upd_dt=graphene.Argument(graphene.Date, description="Test"),
        upd_id=graphene.Argument(graphene.String, description="Test"),
        display_yn=graphene.Argument(graphene.String, description="Test"),
        leaf_yn=graphene.Argument(graphene.String, description="Test"),
        name=graphene.Argument(graphene.String, description="Test"),
        note=graphene.Argument(graphene.String, description="Test"),
        sort_no=graphene.Argument(graphene.Decimal, description="Test"),
        store_id=graphene.Argument(graphene.String, description="Test"),
        upper_display_category_id=graphene.Argument(graphene.String,
                                                    description="Test"),
        template_id=graphene.Argument(graphene.String, description="Test"),
        description="Look up DMS Display Category",
    )

    displaycategorylang = graphene.List(
        DisplayCategoryLangType
    )

    displaycategorylang_id = graphene.Field(DisplayCategoryLangType,
                                            id=graphene.String())

    displaycategorylang_lang = graphene.List(DisplayCategoryLangType,
                                             lang_id=graphene.String(),
                                             display_category_id=graphene.String())

    displaycategorylang_search = graphene.List(
        DisplayCategoryLangType,
        id=graphene.Argument(graphene.Int, description="Test"),
        lang_id=graphene.Argument(graphene.String, description="Test"),
        ins_dt=graphene.Argument(graphene.Date, description="Test"),
        ins_id=graphene.Argument(graphene.String, description="Test"),
        upd_dt=graphene.Argument(graphene.Date, description="Test"),
        upd_id=graphene.Argument(graphene.String, description="Test"),
        name=graphene.Argument(graphene.String, description="Test"),
        note=graphene.Argument(graphene.String, description="Test"),
        display_category_id=graphene.Argument(graphene.String, description="Test"),
        description="Look up DMS Display Category by Language Code"
    )

    displaycategoryproduct = graphene.List(
        DisplayCategoryProductType
    )

    displaycategoryproduct_id = graphene.Field(DisplayCategoryProductType,
                                               id=graphene.String())

    displaycategoryproduct_product = graphene.List(DisplayCategoryProductType,
                                                   product_id=graphene.String())

    displaycategoryproduct_search = graphene.List(
        DisplayCategoryProductType,
        id=graphene.Argument(graphene.Int, description="Test"),
        ins_dt=graphene.Argument(graphene.Date, description="Test"),
        ins_id=graphene.Argument(graphene.String, description="Test"),
        upd_dt=graphene.Argument(graphene.Date, description="Test"),
        upd_id=graphene.Argument(graphene.String, description="Test"),
        display_yn=graphene.Argument(graphene.String, description="Test"),
        sort_no=graphene.Argument(graphene.Decimal, description="Test"),
        display_category_id=graphene.Argument(graphene.String, description="Test"),
        product_id=graphene.Argument(graphene.String, description="Test"),
        description="Look up DMS Display Category Product",
    )

    def resolve_display(self, info, **data):
        return resolve_display(info)

    def resolve_display_id(self, info, id):
        return resolve_display_id(id)

    def resolve_display_search(self, info, **data):
        return resolve_display_search(data)

    def resolve_displaycategory(self, info, **data):
        return resolve_displaycategory(info)

    def resolve_displaycategory_id(self, info, id):
        return resolve_displaycategory_id(id)

    def resolve_displaycategory_search(self, info, **data):
        return resolve_displaycategory_search(data)

    def resolve_displaycategorylang(self, info, **data):
        return resolve_displaycategorylang(info)

    def resolve_displaycategorylang_id(self, info, id):
        return resolve_displaycategorylang_id(id)

    def resolve_displaycategorylang_lang(self, info, **data):
        return resolve_displaycategorylang_lang(data)

    def resolve_displaycategorylang_search(self, info, **data):
        return resolve_displaycategorylang_search(data)

    def resolve_displaycategoryproduct(self, info, **data):
        return resolve_displaycategoryproduct(info)

    def resolve_displaycategoryproduct_id(self, info, id):
        return resolve_displaycategoryproduct_id(id)

    def resolve_displaycategoryproduct_product(self, info, **data):
        return resolve_displaycategoryproduct_product(data['product_id'
                                                      ])

    def resolve_displaycategoryproduct_search(self, info, **data):
        return resolve_displaycategoryproduct_search(data)
