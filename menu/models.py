from django.db import models
from restaurants.models import Restaurant
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta :
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=128,null=False,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="media/dishes",blank=False,null=False)
    note = models.IntegerField(default=0)
    number_of_review = models.IntegerField(default=0)

    def get_absolute_url(self) :
        return reverse("add_to_cart",kwargs={"slug" : self.slug})
    
    class Meta :
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name