from django.test import TestCase
from graphene import Schema
from graphql_relay import to_global_id

from myapp.schema import Query, Mutation


class TestOneToOneSchema(TestCase):

    def test_one_to_one_schema(self):
        schema = Schema(query=Query, mutation=Mutation)

        mutation = """
            mutation{
              createPerson(input: {
                name:"Tormod",
                age: 32,
                bankAccount: {
                  accountNumber: "123456",
                  balance: 100
                }
              }){
                person{
                  id
                  name
                  bankAccount{
                    id
                    accountNumber
                    balance
                  }
                }
              }
              createBankAccount(input: {
                balance: 1,
                accountNumber: "654321"
                person:{
                  name: "Tormod",
                  age: 32
                }
              }){
                bankAccount{
                  id
                  accountNumber
                  balance
                  person{
                    id
                    name
                  }
                }
              }
            }
        """

        result = schema.execute(mutation)

        self.assertEqual(result.data, {
            'createPerson': {
                'person': {
                    'id': to_global_id('PersonNode', '1'),
                    'name': 'Tormod',
                    'bankAccount': {
                        'id': to_global_id('BankAccountNode', '1'),
                        'accountNumber': '123456',
                        'balance': 100,
                    }
                }
            },
            'createBankAccount': {
                'bankAccount': {
                    'id': to_global_id('BankAccountNode', '2'),
                    'accountNumber': '654321',
                    'balance': 1,
                    'person': {
                        'id': to_global_id('PersonNode', '2'),
                        'name': 'Tormod',
                    }
                }
            },
        })

