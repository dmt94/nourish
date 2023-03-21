from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('categories/', views.CategoryList, name='categories'),
  path('accounts/signup', views.signup, name='signup'),
  path('restaurants/', views.RestaurantList.as_view(), name='index'),
  path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
  path('favorites/', views.Favorites.as_view(), name='favorites'),
  path('restaurants/<int:restaurant_id>/', views.detailsview, name='detail'),
]