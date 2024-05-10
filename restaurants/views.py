from django.shortcuts import render, get_object_or_404
from restaurants.models import Restaurant
from menu.models import Dish
from django.db.models import Count
from reviews.models import Review
# Create your views here.

def index(request) :
    most_reviewed_restaurants = Restaurant.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews')[:5]    
    
    datas = {
        "most_liked_restaurants" : most_reviewed_restaurants
    }
    return render(request,'restaurants/index.html',context=datas)




def show(request,slug) :
    restaurant = get_object_or_404(Restaurant,slug=slug)
    dishes = restaurant.dish_set
    latest_reviews = restaurant.reviews.all().order_by('-id')[:10]
    all_reviews = restaurant.reviews.all().order_by('-id')

    
    restaurants_datas = {
        'restaurant' : restaurant,
        'latest_reviews' : latest_reviews,
        'dishes' : dishes,
        'all_reviews' : all_reviews,
        'land' : 4 
    }
    return render(request,'restaurants/show.html',restaurants_datas),





# def feed(request):
#     # Retrieve most liked restaurants
#     most_liked_restaurants = Restaurant.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

#     # Retrieve most liked dishes
#     most_liked_dishes = Dish.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]

#     # Retrieve nearest restaurants (You need to implement this based on user location)
#     nearest_restaurants = Restaurant.objects.all()[:5]

#     # Retrieve vegetarian food
#     vegetarian_dishes = Dish.objects.filter(is_vegetarian=True)[:5]

#     # Retrieve breakfasts
#     breakfast_dishes = Dish.objects.filter(category='Breakfast')[:5]

#     # Retrieve seafood
#     seafood_dishes = Dish.objects.filter(category='Seafood')[:5]

#     # Pass the data to the template
#     return render(request, 'feed.html', {
#         'most_liked_restaurants': most_liked_restaurants,
#         'most_liked_dishes': most_liked_dishes,
#         'nearest_restaurants': nearest_restaurants,
#         'vegetarian_dishes': vegetarian_dishes,
#         'breakfast_dishes': breakfast_dishes,
#         'seafood_dishes': seafood_dishes,
#     })