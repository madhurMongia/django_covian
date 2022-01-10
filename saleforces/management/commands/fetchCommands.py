import httpx
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.conf import settings
from saleforces.models import User
from django.apps import apps
from pprint import pprint
from core.settings import config
@transaction.atomic
def bulk_save(model,data):
    for entity in data:
        entity.pop('attributes')
        instance = model.objects.create(**entity)
        instance.save()

def get_headers():
    params = {
        'grant_type' : config.get('AUTHENTICATION_HEADERS','GRANT_TYPE'),
        'client_id' :  config.get('AUTHENTICATION_HEADERS','CLIENT_ID'),
        'client_secret' : config.get('AUTHENTICATION_HEADERS','CLIENT_SECRET'),
        'username' : config.get('AUTHENTICATION_HEADERS','USERNAME'),
        'password' : config.get('AUTHENTICATION_HEADERS','PASSWORD'),
    }
    raw = httpx.post('https://ymca-1c-dev-ed.my.salesforce.com/services/oauth2/token', params=params)
    headers = {
    'Authorization' : 'Bearer ' + raw.json()['access_token'],
    'X-PrettyPrint':'1'
    }
    return headers
class Command(BaseCommand):
    def fetch(self,entity):
        model = apps.get_model('saleforces',entity)
        model.objects.all().delete()
        cols = ','.join([field.name for field in model._meta.get_fields()])
        entityList = httpx.get('https://ymca-1c-dev-ed.my.salesforce.com/services/data/v53.0/query', headers=get_headers(), params={'q':'SELECT '+cols+' FROM ' + entity.title()})

        bulk_save(model,entityList.json()['records'])
        self.stdout.write(self.style.SUCCESS(f'Successfully {entityList.json()["totalSize"]} {entity} fetched'))
    
    def add_arguments(self, parser):
        parser.add_argument('entity', type=str, help='Indicates the if User/Account/Contacts to be Fetched')
    def handle(self,*args,**options):
            if(options['entity']):
                self.fetch(options['entity'])
            else:
               self.fetch()
