from django.db import models
from django.urls import reverse
from foodieFinder import settings
# Create your models here.
# from menu.models import Category

class RestaurantDomain(models.Model) :
    name = models.CharField(max_length=50)
    
    class Meta :
        verbose_name_plural = 'restaurants domains'

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128,unique=True,null=False)
    # admin = models.ForeignKey(default=1, related_name='managed_restaurant',on_delete=models.CASCADE,to=settings.U)
    address = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)

    opening_hours =  models.CharField(max_length=20)
    opening_hours_weekend = models.CharField(max_length=20)
    delivery_time = models.CharField(max_length=20)
    domains = models.ManyToManyField(RestaurantDomain)
    restaurant_lat = models.CharField(max_length=255,default=0)
    restaurant_long = models.CharField(max_length=255,default=0)

    thumbnail = models.ImageField(upload_to="media/restaurants",blank=False,null=False) 

    def get_absolute_url(self) :
        return reverse("restaurants:show",kwargs={"slug" : self.slug})
    # Autres champs pertinents pour les restaurants

    def __str__(self):
        return self.name