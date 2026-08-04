import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Automatically creates an admin superuser if it does not exist'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME', 'admin').strip()
        email = os.environ.get('ADMIN_EMAIL', 'jahan242-15-846@diu.edu.bd').strip()
        password = os.environ.get('ADMIN_PASSWORD', None).strip()

        user = User.objects.filter(username=username).first()
        if not user:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' password updated successfully!"))
