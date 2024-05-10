from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, get_object_or_404
from django.urls import reverse
# Create your views here.
from menu.models import Dish
from orders.models import Order, Cart


def index(request) :
    return render(request,'foodief/index.html')



def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    order, created = Order.objects.get_or_create(user=request.user, items=dish, ordered=False)
    order.quantity += 1
    order.save()
    cart.orders.add(order)
    return redirect('cart')

def remove_from_cart(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = Cart.objects.get(user=request.user)
    cart.orders.remove(order)
    order.delete()
    return redirect('cart')

def cart(request):
    cart = Cart.objects.get(user=request.user)
    orders = cart.orders.all()
    return render(request, 'orders/cart.html', {'orders': orders, 'cart': cart})

# def order_checkout(request):
#     cart = Cart.objects.get(user=request.user)
#     orders = cart.orders.filter(ordered=False)
    
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # Process the form and create the final order
#             # Set the 'ordered' and 'ordered_date' fields for each order in the cart
#             for order in orders:
#                 order.ordered = True
#                 order.ordered_date = timezone.now()
#                 order.save()
            
#             # Clear the cart
#             cart.orders.clear()
            
#             return redirect('order_confirmation')
#     else:
#         form = OrderForm()
    
#     return render(request, 'orders/checkout.html', {'form': form, 'cart': cart, 'orders': orders})

def order_confirmation(request):
    return render(request, 'orders/confirmation.html')
