from django.core.management.base import BaseCommand
from sport_equipment.factories import CategoryFactory, EquipmentFactory
from user.models import MyUser
from django.contrib.auth.models import Group, Permission
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    # help = 'Factory Boy examples'

    def handle(self, *args, **options):
        MyUser.objects.all().delete()
        MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        MyUser.objects.create_user('auth', 'auth@auth.com', 'auth123456')
        MyUser.objects.create_user('moderator', 'moderator@moderator.com', 'moderator123456')
        staff = MyUser.objects.create_user('staff', 'staff@staff.com', 'staff123456', is_staff=True)
        token = Token.objects.create(user=staff)
        print(token.key)


        # group = Group.objects.create(name='moderators')
        # permission = Permission.objects.get(name='category_view')
        # Permission.objects.get(name='category_add')
        # Permission.objects.get(name='category_change')
        #
        # Permission.objects.create(name='can moderete smf')
        #
        # group.premission.add(permission)

        # Правильный пример кода
        # content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
        # permission = Permission.objects.create(codename='can_publish',
        #                                        name='Can Publish Posts',
        #                                        content_type=content_type)
        # user = User.objects.get(username='duke_nukem')
        # group = Group.objects.get(name='wizard')
        # group.permissions.add(permission)
        # user.groups.add(group)


