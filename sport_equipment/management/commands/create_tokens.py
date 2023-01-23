from django.core.management.base import BaseCommand
from sport_equipment.factories import CategoryFactory, EquipmentFactory
from user.models import MyUser
from django.contrib.auth.models import Group, Permission
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    # help = 'Factory Boy examples'

    def handle(self, *args, **options):
        staff = MyUser.objects.get(username='staff')
        token = Token.objects.create(user=staff)
        print(token.key)