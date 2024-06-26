from datetime import timezone
from django.db import models
from users.models import User
from menu.models import Dish
from foodieFinder.settings import AUTH_USER_MODEL
# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    item = models.ForeignKey(Dish, on_delete=models.CASCADE,related_name='item')
    quantity =  models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.item.name} ({self.quantity})"
    


class Cart(models.Model) :
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs) :
        for order in self.orders.all() :
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)
