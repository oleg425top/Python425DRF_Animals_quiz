import os

from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admindrf@web.top',
            first_name='Admin',
            last_name='Adminov',
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        admin.set_password(os.getenv("SUPERUSER_PASSWORD"))
        admin.save()
        print('Admin Created!!')

        moderator = User.objects.create(
            email='moderatordrf@web.top',
            first_name='Moderator',
            last_name='Moderatorov',
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )
        moderator.set_password(os.getenv("MODERATOR_PASSWORD"))
        moderator.save()
        print('Moderator Created!!')

        user = User.objects.create(
            email='userdrf@web.top',
            first_name='Member',
            last_name='Memberov',
            role=UserRoles.MEMBER,
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        user.set_password(os.getenv("MEMBER_PASSWORD"))
        user.save()
        print('User Created!!')
