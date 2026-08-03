from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


class Index(View):

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
        else:
            cart = {}
            if product and not remove and not clear_item:
                cart[product] = 1

        request.session['cart'] = cart
        if request.POST.get('buy_now'):
            return redirect('/cart')
        return redirect('homepage')

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    query = request.GET.get('query')

    if query:
        products = Products.search_products(query.strip())
    elif categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['query'] = query

    return render(request, 'index.html', data)
