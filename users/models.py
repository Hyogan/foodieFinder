from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurants.models import Restaurant
# Create your models here.

class User(AbstractUser) :
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128)
    role = models.CharField(max_length=128,default='standard')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) :
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username + "'s profile"


