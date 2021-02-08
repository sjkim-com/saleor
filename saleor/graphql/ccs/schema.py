import graphene

from .mutation.business import BusinessInsert, BusinessUpdate, BusinessDelete
from .mutation.jwt import CreateToken
from .mutation.user import UserCreate, UserCreateNew
from .resolver import resolve_business, resolve_business_id, resolve_business_add1, \
    resolve_business_search
from .types import Business


class CcsQueries(graphene.ObjectType):
    business = graphene.List(
        Business
    )

    business_id = graphene.Field(Business, id=graphene.String())

    business_add1 = graphene.Field(Business, address1=graphene.String())

    business_search = graphene.List(
        Business,
        business_no=graphene.Argument(graphene.ID, description="Test"),
        ins_dt=graphene.Argument(graphene.String, description="Test"),
        ins_id=graphene.Argument(graphene.String, description="Test"),
        upd_dt=graphene.Argument(graphene.String, description="Test"),
        upd_id=graphene.Argument(graphene.String, description="Test"),
        account_no=graphene.Argument(graphene.String, description="Test"),
        address1=graphene.Argument(graphene.String, description="Test"),
        address2=graphene.Argument(graphene.String, description="Test"),
        address3=graphene.Argument(graphene.String, description="Test"),
        address4=graphene.Argument(graphene.String, description="Test"),
        bank_name=graphene.Argument(graphene.String, description="Test"),
        business_condition=graphene.Argument(graphene.String, description="Test"),
        business_state_cd=graphene.Argument(graphene.String, description="Test"),
        business_tax_type_cd=graphene.Argument(graphene.String, description="Test"),
        business_type=graphene.Argument(graphene.String, description="Test"),
        business_type_cd=graphene.Argument(graphene.String, description="Test"),
        contract_end_dt=graphene.Argument(graphene.String, description="Test"),
        contract_start_dt=graphene.Argument(graphene.String, description="Test"),
        country_id=graphene.Argument(graphene.String, description="Test"),
        country_no=graphene.Argument(graphene.String, description="Test"),
        depositor_name=graphene.Argument(graphene.String, description="Test"),
        erp_business_id=graphene.Argument(graphene.String, description="Test"),
        fax=graphene.Argument(graphene.String, description="Test"),
        manager_email=graphene.Argument(graphene.String, description="Test"),
        manager_name=graphene.Argument(graphene.String, description="Test"),
        manager_phone1=graphene.Argument(graphene.String, description="Test"),
        manager_phone2=graphene.Argument(graphene.String, description="Test"),
        memo=graphene.Argument(graphene.String, description="Test"),
        name=graphene.Argument(graphene.String, description="Test"),
        note=graphene.Argument(graphene.String, description="Test"),
        overseas_purchase_yn=graphene.Argument(graphene.String, description="Test"),
        phone=graphene.Argument(graphene.String, description="Test"),
        reg_no=graphene.Argument(graphene.String, description="Test"),
        rep_name=graphene.Argument(graphene.String, description="Test"),
        req_user_id=graphene.Argument(graphene.String, description="Test"),
        req_user_pwd=graphene.Argument(graphene.String, description="Test"),
        sale_type_cd=graphene.Argument(graphene.String, description="Test"),
        sales_email=graphene.Argument(graphene.String, description="Test"),
        sales_name=graphene.Argument(graphene.String, description="Test"),
        sales_phone1=graphene.Argument(graphene.String, description="Test"),
        sales_phone2=graphene.Argument(graphene.String, description="Test"),
        store_id=graphene.Argument(graphene.String, description="Test"),
        supply_item=graphene.Argument(graphene.String, description="Test"),
        user_id=graphene.Argument(graphene.String, description="Test"),
        zip_cd=graphene.Argument(graphene.String, description="Test"),
        sf_id=graphene.Argument(graphene.String, description="Test"),
        description="Look up business",
    )

    def resolve_business(self, info, **data):
        # return graphene.Node.get_node_from_global_id(info, id, Test)
        print(data)
        return resolve_business(info)

    def resolve_business_id(self, info, id):
        return resolve_business_id(id)

    def resolve_business_add1(self, info, address1):
        return resolve_business_add1(address1)

    def resolve_business_search(self, info, **data):
        return resolve_business_search(data)


class CcsMutations(graphene.ObjectType):
    token_create = CreateToken.Field()
    user_create = UserCreateNew.Field()
    business_insert = BusinessInsert.Field()
    business_update = BusinessUpdate.Field()
    business_delete = BusinessDelete.Field()
