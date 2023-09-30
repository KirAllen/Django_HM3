from django.core.management.base import BaseCommand
from app2.models import Customer

class Command(BaseCommand):

    help = "Create User."

    def handle(self, *args, **options):
        customer = Customer(name='Anton', email='Anton@mail.ru',phone_number=899944433,adress='Moscow',date_register='2021-2-19', password="qwerty123",age=27 )

        customer.save()
        self.stdout.write(f'{customer}')
