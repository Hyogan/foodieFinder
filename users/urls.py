from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('signup',views.register_view, name='user.signup'),
    path('login',views.authenticate_view, name='user.login'),
    path('logout',views.logout_user, name='user.logout'),
]