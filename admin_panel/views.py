
# Create your views here.
from django.shortcuts import render, get_object_or_404
from users.models  import User
from restaurants.models import Restaurant
from orders.models import Order
from menu.models import Dish
# Create your views here.

def index(request) :
    user = request.user
    restaurant = get_object_or_404(Restaurant, pk=user.restaurant.id)
    orders_count = Order.objects.filter(item__restaurant=restaurant).count()
    dishes_count = restaurant.dish_set.count()
    # activities_count = restaurant.activities.count()
    activities_count = 10
    
    counts_data = {
        'orders_count': orders_count,
        'dishes_count': dishes_count,
        'activities_count': activities_count
    }
    return render(request,'admin_panel/pages/dashboard.html',context=counts_data)

def activities(request) :
    return render(request,'admin_panel/pages/activities.html')

def users(request) :
    return render(request,'admin_panel/pages/users.html')

def orders(request) :
    return render(request,'admin_panel/pages/orders.html')

def menu(request) :
    restaurant_id = request.user.restaurant.id
    restaurant_dishes = Dish.objects.filter(restaurant_id=restaurant_id)
    return render(request,'admin_panel/pages/menu.html',{'restaurant_dishes' : restaurant_dishes})

def reviews(request) :
    return render(request,'admin_panel/pages/reviews.html')

def profile(request) :
    return render(request,'admin_panel/pages/profile.html')

def messages(request) :
    return render(request,'admin_panel/pages/messages.html')
