import graphene

from .resolver import *
from .types import ProductOrgType


class PmsQueries(graphene.ObjectType):
    # category = graphene.Field(Category)

    # def resolve_category(self, info):
    #     qs = models.Category.objects.all()
    #     return qs

    # All Product List
    product = graphene.List(ProductOrgType)

    def resolve_product(self, info, **data):
        print(data)
        return resolve_product(info)

    product_search = graphene.List(ProductOrgType,
                                   name=graphene.Argument(graphene.String, description="Product Name"),
                                   businessProductIds=graphene.Argument(graphene.String, description="Product Id"),
                                   businessSaleproductIds=graphene.Argument(graphene.String, description="SaleProduct Id"),
                                   productTypeCds=graphene.Argument(graphene.String, description="Product Type Cds"),
                                   saleStateCds=graphene.Argument(graphene.String, description="sale State Cds"),
                                   categoryId=graphene.Argument(graphene.String, description="Category Id"),
                                   business_no=graphene.Argument(graphene.Int, description="Business No"),
                                   startDate=graphene.Argument(graphene.Date, description="Start Date"),
                                   endDate=graphene.Argument(graphene.Date, description="End Date"),
                                   # page=graphene.Argument(graphene.Int, description="Page"),
                                   # display_type_cd=graphene.Argument(graphene.String, description="Test"),
                                   # display_yn=graphene.Argument(graphene.String, description="Test"),
                                   # leaf_yn=graphene.Argument(graphene.String, description="Test"),
                                   # name=graphene.Argument(graphene.String, description="Test"),
                                   # sort_no=graphene.Argument(graphene.Decimal, description="Test"),
                                   # store_id=graphene.Argument(graphene.String, description="Test"),
                                   # upper_display_id=graphene.Argument(graphene.String, description="Test"),
                                   # use_yn=graphene.Argument(graphene.String, description="Test"),
                                   description="Look up PMS Display",
                                   )

    def resolve_product_search(self, info, **data):
        return resolve_product_search(data)
