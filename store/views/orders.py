from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})

    def post(self, request):
        order_id = request.POST.get('order_id')
        message = request.POST.get('message', '').strip()
        if order_id and message:
            try:
                order = Order.objects.get(id=order_id)
                order.customer_message = message
                order.save()
            except Exception as e:
                print(e)
        return redirect('/orders')
