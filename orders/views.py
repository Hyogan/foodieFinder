from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, get_object_or_404
from django.urls import reverse
# Create your views here.
from menu.models import Dish
from orders.models import Order, Cart
from django.contrib.auth.decorators import login_required


def index(request) :
    return render(request,'foodief/index.html')

@login_required
def add_to_cart(request, slug):
    user = request.user
    dish = get_object_or_404(Dish, slug=slug)

    ## Creating a new cart if not existing and checking the quantity of the order
    cart, _ = Cart.objects.get_or_create(user=user)
    order, is_created = Order.objects.get_or_create(user=user,item=dish,ordered=False)

    if is_created:
        cart.orders.add(order)
        order.save()
    else :
        order.quantity += 1
        order.save()
    
    return redirect('cart')

@login_required
def remove_from_cart(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = Cart.objects.get(user=request.user)
    cart.orders.remove(order)
    order.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    orders = cart.orders.all()
    count_el = cart.orders.count()
    total_price = sum(order.item.price * order.quantity for order in orders)
    cart_datas = {
        "cart" : cart,
        "orders" : orders,
        "count_el" : count_el,
        "total_price" : total_price
    }
    return render(request, 'order/cart.html', context=cart_datas)



@login_required
def update_cart(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = Cart.objects.get(user=request.user)
    
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
        if new_quantity > 0:
            order.quantity = new_quantity
            order.save()
    
    return redirect('cart')


@login_required
def order_confirmation(request):
    return render(request, 'orders/confirmation.html')
