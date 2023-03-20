from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('restaurants/', views.RestaurantList.as_view(), name='index'),
]