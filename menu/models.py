from django.db import models
from restaurants.models import Restaurant
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=128,null=False,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="media/dishes",blank=False,null=False)

    def __str__(self):
        return self.name