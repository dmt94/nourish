from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('restaurants/', views.RestaurantList.as_view(), name='index'),
  path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
  # path('favorites/', views.restaurants_index, name='index'),
]