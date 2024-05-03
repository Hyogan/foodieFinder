from django.contrib import admin
from users.models import User, Profile
from menu.models import Category, Dish
from restaurants.models import Restaurant
from orders.models import Order, Cart
from reviews.models import Review
# Register your models here.


class UserAdmin(admin.ModelAdmin) :
    list_display = ['username','email']
    
class ProfileAdmin(admin.ModelAdmin) :
    list_display = ['user','address','phone_number']

class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['name']

class DishAdmin(admin.ModelAdmin) :
    list_display = ['restaurant','category','name','price','slug']

class OrderAdmin(admin.ModelAdmin) :
    list_display = ['user','quantity','ordered','status']

class CartAdmin(admin.ModelAdmin) :
    list_display = ['user']


class ReviewAdmin(admin.ModelAdmin) :
    list_display = ['restaurant','user','rating','comment']

class RestaurantAdmin(admin.ModelAdmin) :
    list_display = ['name','address','description','phone_number']


admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Dish,DishAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Restaurant,RestaurantAdmin)