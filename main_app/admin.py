from django.contrib import admin
# can make admin (createsuperuser) after migrating models
# create initial model first

# Register your models here.
from .models import Category, Review, Restaurant

# Register your models here
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Restaurant)