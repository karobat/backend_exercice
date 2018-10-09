import graphene

from graphene_django.types import DjangoObjectType
from graphene import InputObjectType

from shoppinglist.models import ShoppingList, ShoppingListItem

class ShoppingListType(DjangoObjectType):
    class Meta:
        model = ShoppingList

class ShoppingListItemType(DjangoObjectType):
    class Meta:
        model = ShoppingListItem

class CreateShoppingList(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
    
    def mutate(self, info, name):
        shopping_list = ShoppingList(name=name)
        shopping_list.save()

        return CreateShoppingList(id=shopping_list.id, name=shopping_list.name)

class DeleteShoppingList(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        list_id = graphene.Int(required=True)
    
    def mutate(self, info, listId):
        shopping_list = ShoppingList.objects.get(pk=list_id)
        shopping_list.delete()

        return DeleteShoppingList(name=shopping_list.name)

class AddItem(graphene.Mutation):
    item_id = graphene.Int()
    name = graphene.String()

    class Arguments:
        list_id = graphene.Int(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, list_id, name):
        shopping_list = ShoppingList.objects.get(pk=list_id)
        item = ShoppingListItem(name=name, shopping_list=shopping_list)
        item.save()

        return AddItem(item_id=item.id, name=item.name)

class UpdateItemStatus(graphene.Mutation):
    item_id = graphene.Int()
    name = graphene.String()
    status = graphene.String()

    class Arguments:
        item_id = graphene.Int()
        status = graphene.String()
    
    def mutate(self, info, item_id, status):
        item = ShoppingListItem.objects.get(pk=item_id)
        item.status = status
        item.save()

        return UpdateItemStatus(item_id=item.id, name=item.name, status=item.status)

class Query(object):
    all_shopping_lists = graphene.List(ShoppingListType)
    shopping_list = graphene.Field(ShoppingListType, id=graphene.Int())

    def resolve_all_shopping_lists(self, info, **kwargs):
        return ShoppingList.objects.all()

    def resolve_shopping_list(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ShoppingList.objects.get(pk=id)

        return None

class Mutation(object):
    create_shopping_list = CreateShoppingList.Field()
    delete_shopping_list = DeleteShoppingList.Field()
    add_item = AddItem.Field()
    update_item_status = UpdateItemStatus.Field()
