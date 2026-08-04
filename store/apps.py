from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        try:
            import os
            from django.contrib.auth import get_user_model
            User = get_user_model()
            username = os.environ.get('ADMIN_USERNAME', None).strip()
            password = os.environ.get('ADMIN_PASSWORD', None).strip()
            email = os.environ.get('ADMIN_EMAIL', 'jahan242-15-846@diu.edu.bd').strip()

            user = User.objects.filter(username=username).first()
            if not user:
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
            else:
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.save()
        except Exception:
            pass
