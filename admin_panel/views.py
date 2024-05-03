
# Create your views here.
from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request,'admin_panel/pages/dashboard.html')

def activities(request) :
    return render(request,'admin_panel/pages/activities.html')

def users(request) :
    return render(request,'admin_panel/pages/users.html')

def orders(request) :
    return render(request,'admin_panel/pages/orders.html')

def menu(request) :
    return render(request,'admin_panel/pages/menu.html')

def reviews(request) :
    return render(request,'admin_panel/pages/reviews.html')

def profile(request) :
    return render(request,'admin_panel/pages/profile.html')

def messages(request) :
    return render(request,'admin_panel/pages/messages.html')
