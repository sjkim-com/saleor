from django.db.models import Q
from ...pms import models

############## Product ##################

# テーブルの全データを取得
def resolve_product(info):
    qs = models.Product.objects.all()
    return qs

# テーブルのデータでIDから取得
def resolve_product_id(id):
    qs = models.Product.objects.get(pk=id)
    return qs


def resolve_product_search(info):
    qs = models.Product.objects.filter(
        Q(name=info['name']) |
        Q(product_id=info['businessProductIds']) |
        Q(product_type_cd=info['productTypeCds']) |
        Q(sale_state_cd=info['saleStateCds']) |
        Q(category_id=info['categoryId']) |
        Q(businessNo=info['business_no']) |
        Q(ins_id=info['startDate']) |
        Q(ins_id=info['endDate'])
        # Q(businessSaleproductIds=info['businessSaleproductIds']) |
        # Q(size=info['size']) |
        # Q(page=info['page']) |
        # Q(sort=info['sort']) |
        # Q(langId=info['langId']) |
        # Q(username=info['username'])
    )
    return qs

############## End Product ##################
