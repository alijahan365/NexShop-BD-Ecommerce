from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=150, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    payment_method = models.CharField(max_length=50, default='Cash on Delivery', blank=True)
    transaction_id = models.CharField(max_length=100, default='', blank=True)
    payment_status = models.CharField(max_length=50, default='Pending Verification', blank=True)
    delivery_charge = models.IntegerField(default=0)
    delivery_distance = models.FloatField(default=0.0)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    customer_message = models.CharField (max_length=255, default='', blank=True)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    

