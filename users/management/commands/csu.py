from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда создания суперюзера-администратора.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            first_name="admin",
            last_name="test",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("P@ssw0rd")
        user.save()
