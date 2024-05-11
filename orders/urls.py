from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('dish/<str:slug>/add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('user/cart/details',views.cart,name='cart'),
    path('cart/order/<int:order_id>/delete',views.remove_from_cart,name='order.remove'),
    path('update_cart/<int:order_id>/', views.update_cart, name='update_cart'),
]