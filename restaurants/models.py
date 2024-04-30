from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    # Autres champs pertinents pour les restaurants

    def __str__(self):
        return self.name