from django.shortcuts import render, redirect
from .cart import Cart
from StoreApp.models import Product

# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    cart.add(product=product)

    return redirect("store")

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    cart.delete(product=product)

    return redirect("store")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)

    cart.remove_product(product=product)

    return redirect("store")

def empty_cart(request, product_id):
    cart = Cart(request)
    
    cart.empty_cart()

    return redirect("store")
