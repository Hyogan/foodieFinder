from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('/user/signup',views.register, name='user.signup'),
    path('/user/login',views.authenticate, name='user.login'),
]