from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from perfil.models import Profile

class Command(BaseCommand):
    help = 'Crea perfiles para usuarios existentes que no tienen uno'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(profile__isnull=True)
        for user in users:
            Profile.objects.get_or_create(user=user)
            self.stdout.write(f'Perfil creado para {user.username}') 