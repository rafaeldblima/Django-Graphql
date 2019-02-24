import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from . import models


class FamilyType(DjangoObjectType):
    class Meta:
        model = models.Family
        filter_fields = ['title', 'reference']
        interfaces = (Node,)


class LocationType(DjangoObjectType):
    class Meta:
        model = models.Location
        filter_fields = {
            'reference': ['exact', 'icontains', 'istartswith'],
            'title': ['exact', 'icontains'],
            'description': ['icontains']
        }
        interfaces = (Node,)


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        filter_fields = {
            'sku': ['icontains']
        }
        interfaces = (Node,)


class TransactionType(DjangoObjectType):
    class Meta:
        model = models.Transaction
        filter_fields = ['sku']
        interfaces = (Node,)


class Query(graphene.AbstractType):
    all_families = DjangoFilterConnectionField(FamilyType)
    all_locations = DjangoFilterConnectionField(LocationType)
    all_products = DjangoFilterConnectionField(ProductType)
    all_transactions = DjangoFilterConnectionField(TransactionType)

    product = Node.Field(ProductType)

    # product = graphene.Field(ProductType, id=graphene.Int())
    #
    # def resolve_all_families(self, info, **kwargs):
    #     return models.Family.objects.all()
    #
    # def resolve_all_locations(self, info, **kwargs):
    #     return models.Location.objects.all()
    #
    # def resolve_all_products(self, info, **kwargs):
    #     return models.Product.objects.all()
    #
    # def resolve_all_transactions(self, info, **kwargs):
    #     return models.Transaction.objects.all()
    # #
    # def resolve_product(self, info, **kwargs):
    #     product_id = kwargs.get('id')
    #
    #     if product_id is not None:
    #         return models.Product.objects.get(pk=product_id)
    #
    #     return None
