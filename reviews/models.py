from django.db import models
from restaurants.models import Restaurant
from users.models import User
# Create your models here.



class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()



    def __str__(self):
        return f"Review by {self.user.username} for {self.restaurant.name}"