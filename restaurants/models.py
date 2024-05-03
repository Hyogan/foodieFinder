from django.db import models
from django.urls import reverse
from foodieFinder import settings
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128,unique=True,null=False)
    # admin = models.ForeignKey(default=1, related_name='managed_restaurant',on_delete=models.CASCADE,to=settings.U)
    address = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="media/restaurants",blank=False,null=False) 

    def get_absolute_url(self) :
        return reverse("restaurants:show",kwargs={"slug" : self.slug})
    # Autres champs pertinents pour les restaurants

    def __str__(self):
        return self.name