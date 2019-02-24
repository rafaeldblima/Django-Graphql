import graphene
from graphene import Node
from graphene_django import DjangoObjectType

from . import models


class FamilyType(DjangoObjectType):
    class Meta:
        model = models.Family
        interfaces = (Node,)


class LocationType(DjangoObjectType):
    class Meta:
        model = models.Location
        interfaces = (Node,)


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product


class TransactionType(DjangoObjectType):
    class Meta:
        model = models.Transaction


class Query(graphene.AbstractType):
    all_families = graphene.List(FamilyType)
    all_locations = graphene.List(LocationType)
    all_products = graphene.List(ProductType)
    all_transactions = graphene.List(TransactionType)

    product = graphene.Field(ProductType, id=graphene.Int())

    def resolve_all_families(self, info, **kwargs):
        return models.Family.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        return models.Location.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.all()

    def resolve_all_transactions(self, info, **kwargs):
        return models.Transaction.objects.all()

    def resolve_product(self, info, **kwargs):
        product_id = kwargs.get('id')

        if product_id is not None:
            return models.Product.objects.get(pk=product_id)

        return None
