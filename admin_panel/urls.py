from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('dashboard',views.index, name='admin.index'),
    path('activities',views.activities, name='admin.activities'),
    path('users',views.users, name='admin.users'),
    path('orders',views.orders, name='admin.orders'),
    path('menu',views.menu, name='admin.menu'),
    path('reviews',views.reviews, name='admin.reviews'),
    path('profile',views.profile, name='admin.profile'),
    path('messages',views.messages, name='admin.messages'),
]