from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        ids = list(cart.keys())
        products = Products.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        clear_item = request.POST.get('clear_item')
        cart = request.session.get('cart')

        if cart and product:
            if clear_item and product in cart:
                cart.pop(product)
            else:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1

        request.session['cart'] = cart
        return redirect('cart')
