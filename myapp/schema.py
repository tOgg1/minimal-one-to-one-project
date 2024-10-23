import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django_cud.mutations import DjangoCreateMutation

from myapp.models import Person, BankAccount


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        interfaces = (Node,)


class BankAccountNode(DjangoObjectType):
    class Meta:
        model = BankAccount
        interfaces = (Node,)


class Query(graphene.ObjectType):
    person = Node.Field(PersonNode)
    bank_account = Node.Field(BankAccountNode)



class CreatePersonMutation(DjangoCreateMutation):
    class Meta:
        model = Person
        one_to_one_extras = {
            "bank_account": {
                "type": "auto"
            }
        }


class CreateBankAccountMutation(DjangoCreateMutation):
    class Meta:
        model = BankAccount
        one_to_one_extras = {
            "person": {
                "type": "auto"
            }
        }


class Mutation(graphene.ObjectType):
    create_person = CreatePersonMutation.Field()
    create_bank_account = CreateBankAccountMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
