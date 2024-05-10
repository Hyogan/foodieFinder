from django.shortcuts import render
from restaurants.models import Restaurant
from menu.models import Dish
# Create your views here.

def index(request) :
    return render(request,'core/index.html')