from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('payment_method', 'Cash on Delivery')
        transaction_id = request.POST.get('transaction_id', '')
        customer = request.session.get('customer')
        cart = request.session.get('cart')

        if not cart:
            return redirect('cart')

        products = Products.get_products_by_id(list(cart.keys()))

        try:
            delivery_charge = int(float(request.POST.get('delivery_charge', 0)))
            delivery_distance = round(float(request.POST.get('delivery_distance', 0.0)), 2)
        except (ValueError, TypeError):
            delivery_charge = 0
            delivery_distance = 0.0

        pay_status = 'Unpaid (COD)' if payment_method == 'Cash on Delivery' else 'Pending Verification'

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          payment_method=payment_method,
                          transaction_id=transaction_id,
                          payment_status=pay_status,
                          delivery_charge=delivery_charge,
                          delivery_distance=delivery_distance,
                          quantity=cart.get(str(product.id)))
            order.save()

        # Clear cart
        request.session['cart'] = {}

        # Redirect to orders page to show placed orders
        return redirect('orders')
