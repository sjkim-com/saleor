import graphene

from ....ccs import models
from ...ccs.types import Business


class BusinessInsertInput(graphene.InputObjectType):
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


class BusinessInsert(graphene.Mutation):
    businessObj = graphene.Field(Business)

    class Arguments:
        input = BusinessInsertInput(
            description="Fields required to create a business.", required=True
        )

    class Meta:
        description = "Register a new business item."
        model = models.Business

    @classmethod
    def get_type_for_model(cls):
        return Business

    @classmethod
    def mutate(cls, root, info, **data):
        business = models.Business.objects.create(**data['input'])
        business.save()
        return BusinessInsert(businessObj=business)


class BusinessUpdate(graphene.Mutation):
    updated = graphene.Boolean()
    businessObj = graphene.Field(Business)

    class Arguments:
        businessNo = graphene.Int(required=True)
        input = BusinessInsertInput(
            description="Fields required to Update a user.", required=True
        )

    @classmethod
    def get_type_for_model(cls):
        return Business

    @classmethod
    def mutate(cls, root, info, **data):
        upd_ins = models.Business.objects.get(pk=data['businessNo'])
        if upd_ins:

            business = models.Business.objects.create(**data['input'])
            business.business_no = data['id']
            business.save()
            return BusinessUpdate(updated=True, businessObj=business)
        return BusinessUpdate(updated=False, businessObj=None)


class BusinessDelete(graphene.Mutation):
    updated = graphene.Boolean()

    class Arguments:
        businessNo = graphene.Int(required=True)

    @classmethod
    def get_type_for_model(cls):
        return Business

    @classmethod
    def mutate(cls, root, info, **data):
        del_ins = models.Business.objects.get(pk=data['businessNo'])
        if del_ins:
            del_ins.delete()
            return BusinessDelete(updated=True)
        return BusinessDelete(updated=False)
