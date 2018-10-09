import graphene

import shoppinglist.schema

class Query(shoppinglist.schema.Query, graphene.ObjectType):
    pass

class Mutation(shoppinglist.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)