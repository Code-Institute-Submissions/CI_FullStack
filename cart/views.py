from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    Returning the cart's page and current contents
    """
    return render(request, 'cart.html')


def add_to_cart(request, product_id):
    """
    Add a quantity to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """
    Adjust the quantity of a product to the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop[id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))