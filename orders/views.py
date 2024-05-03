from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, get_object_or_404
from django.urls import reverse
# Create your views here.
from menu.models import Dish
from orders.models import Order, Cart


def index(request) :
    return render(request,'foodief/index.html')



def add_to_cart(request,slug) :
    user = request.user
    product = get_object_or_404(Dish,slug=slug)
    if product.stock > 0 :
        cart, _ = Cart.objects.get_or_create(user=user)
        order, is_created = Order.objects.get_or_create(user=user,ordered=False,product=product)
        if is_created :
            cart.orders.add(order)
            cart.save()
        else :
            order.quantity += 1
            order.save()

    return redirect(reverse("core:index",kwargs={"slug" : slug}))

def cart(request) :
    cart = get_object_or_404(Cart, user=request.user)
    return render(request,'order/cart.html',context={"orders" : cart.orders.all()})


def delete_cart(request) :
    pass
    cart = request.user.cart
    # if cart := request.user.cart 
    if cart :
        cart.delete()

    return redirect('core:index')

