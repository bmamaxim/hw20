import json

from django.core.management import BaseCommand

from materials.models import Direction, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            pay_for_create = []

            for model in data:
                if model['model'] == "users.payment":
                    pay_for_create.append(Payment(user=User.objects.get(pk=model['fields']['user']),
                                                  direction=Direction.objects.get(pk=model['fields']['direction']),
                                                  lesson=Lesson.objects.get(pk=model['fields']['direction']),
                                                  payment_sign=model['fields']['payment_sign'],
                                                  payment_sum=model['fields']['payment_sum'],
                                                  payment_method=model['fields']['payment_method'],
                                                  payment_date=model['fields']['payment_date']))

            Payment.objects.bulk_create(pay_for_create)
