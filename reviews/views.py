from django.shortcuts import render

# Create your views here.

# reviews/views.py

def review_create_view(request, restaurant_id):
    context = {

    }
    # Logic to create a review for a restaurant
    return render(request, 'review_create.html', context)

def index(request) :
    pass

def review_list_view(request, restaurant_id):
    context = {
        
    }
    # Logic to retrieve and display reviews for a restaurant
    return render(request, 'review_list.html', context)
