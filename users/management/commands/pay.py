import json

from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            pay_for_create = []

            for model in data:
                if model['model'] == 'user.payment':
                    pay_for_create.append(model)

            Payment.objects.bulk_create(pay_for_create)
