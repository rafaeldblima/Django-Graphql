import graphene

import inventory.schema


class Query(inventory.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query)
