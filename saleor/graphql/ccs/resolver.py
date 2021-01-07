from django.db.models import Q

from ...ccs import models

BUSINESS_SEARCH_FIELDS = (
    'business_no',
    'ins_dt',
    'ins_id',
    'upd_dt',
    'upd_id',
    'account_no',
    'address1',
    'address2',
    'address3',
    'address4',
    'bank_name',
    'business_condition',
    'business_state_cd',
    'business_tax_type_cd',
    'business_type',
    'business_type_cd',
    'contract_end_dt',
    'contract_start_dt',
    'country_id',
    'country_no',
    'depositor_name',
    'erp_business_id',
    'fax',
    'manager_email',
    'manager_name',
    'manager_phone1',
    'manager_phone2',
    'memo',
    'name',
    'note',
    'overseas_purchase_yn',
    'phone',
    'reg_no',
    'rep_name',
    'req_user_id',
    'req_user_pwd',
    'sale_type_cd',
    'sales_email',
    'sales_name',
    'sales_phone1',
    'sales_phone2',
    'store_id',
    'supply_item',
    'user_id',
    'zip_cd',
    'sf_id',
)


def resolve_business(info):
    print("get all")
    qs = models.Business.objects.all()
    print(qs)
    return qs


def resolve_business_id(id):
    qs = models.Business.objects.get(pk=id)
    return qs


def resolve_business_add1(add1):
    qs = models.Business.objects.get(address1=add1)
    return qs

def resolve_business_search(info):
    print(info)

    qs = models.Business.objects.filter(Q(address1=info['address1'])|Q(address2=info['address2']))
    return qs
