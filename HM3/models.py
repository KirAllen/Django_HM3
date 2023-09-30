from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.TextField(max_length=300)
    password = models.CharField(max_length=100)
    date_register = models.DateTimeField()
    age = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    description = models.TextField()
    date_upd = models.DateTimeField()
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.TextField(max_length=300)
    date_order = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
            return f'Customer: {self.customer.name}, products: {self.products},  date_ordered: {self.date_order}, total_price: {self.total_price}'