from django.core.management.base import BaseCommand

from .models import Customer, Order
from random import randint


class Command(BaseCommand):
    help = "Generate Arguments."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count+1):
            customer = Customer(name=f'Customer_{i}',
                                email=f'Customer_{i}_mail.ru',
                                phone_number=randint(1000, 9999),
                                date_register=f"{randint(1980,2023)}-{randint(1,12)}-{randint(1,30)}", age=randint(18,99))
            customer.save()
            for j in range(1, count+1):
                order = Order(customer=customer, products=f'Product_{randint(1,9)}',
                                date_order=f"{randint(2022,2023)}-{randint(1,12)}-{randint(1,30)}",
                                total_price = randint(2000, 10_000)/randint(2,4)
                                  )
                order.save()