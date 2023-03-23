from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

#This is giselles comment
#This is daevahs comment
#This is Sumis comment
#this is Adas comment
#This is jennys comment
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # add user_id FK column
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # # create a M:M relationship with Review
    # reviews = models.ManyToManyField(Review)
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='restaurants', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)