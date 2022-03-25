# Marshmallow example
import os
import pprint
from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings


class Thing(DynaModel):
    class Table:
        resource_kwargs = {
            'region_name': 'us-east-1'
        }
        name = 'tableLambda'.format(env=os.environ.get('ENVIRONMENT', 'dev'))
        hash_key = 'data'
        sort_key = 'hora'
       # read = 10
       # write = 10

    class Schema:
        data = fields.String(required=True)
        hora = fields.String(required=True)
        corrente = fields.Number()
        temperatura = fields.Number()
        tensao = fields.Number()

        #coluna = fields.List(cls_or_instance=fields.Float())

    def ver_dados(self, data=True, hora=True, corrente=True, temperatura=True, tensao=True):
        print("{data}\n{hora}\n{corrente}\n{temperatura}\n{tensao}".format(
           data=self.data,
           hora=self.hora,
           corrente=self.corrente,
           temperatura=self.temperatura,
           tensao=self.tensao

        ))


if __name__ == '__main__':
    thing = Thing.get(data="15/11/2021" , hora="15:23")
    if thing:
        print("\nDados do Item requiridos com sucesso:\n")
        print(thing.ver_dados())

