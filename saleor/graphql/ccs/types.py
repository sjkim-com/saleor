import graphene

from ...ccs.models import Business
from ..core.connection import CountableDjangoObjectType


class Business(CountableDjangoObjectType):
    class Meta:
        model = Business
        fields = ('business_no',
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
                  'sf_id')

    business_no = graphene.Int()
    ins_dt = graphene.Date()
    ins_id = graphene.String()
    upd_dt = graphene.Date()
    upd_id = graphene.String()
    account_no = graphene.String()
    address1 = graphene.String()
    address2 = graphene.String()
    address3 = graphene.String()
    address4 = graphene.String()
    bank_name = graphene.String()
    business_condition = graphene.String()
    business_state_cd = graphene.String()
    business_tax_type_cd = graphene.String()
    business_type = graphene.String()
    business_type_cd = graphene.String()
    contract_end_dt = graphene.Date()
    contract_start_dt = graphene.Date()
    country_id = graphene.String()
    country_no = graphene.String()
    depositor_name = graphene.String()
    erp_business_id = graphene.String()
    fax = graphene.String()
    manager_email = graphene.String()
    manager_name = graphene.String()
    manager_phone1 = graphene.String()
    manager_phone2 = graphene.String()
    memo = graphene.String()
    name = graphene.String()
    note = graphene.String()
    overseas_purchase_yn = graphene.String()
    phone = graphene.String()
    reg_no = graphene.String()
    rep_name = graphene.String()
    req_user_id = graphene.String()
    req_user_pwd = graphene.String()
    sale_type_cd = graphene.String()
    sales_email = graphene.String()
    sales_name = graphene.String()
    sales_phone1 = graphene.String()
    sales_phone2 = graphene.String()
    store_id = graphene.String()
    supply_item = graphene.String()
    user_id = graphene.String()
    zip_cd = graphene.String()
    sf_id = graphene.String()
