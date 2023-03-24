from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('categories/', views.CategoryList, name='categories'),
  path('accounts/signup', views.signup, name='signup'),
  path('restaurants/', views.RestaurantList.as_view(), name='index'),
  path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
  path('favorites/', views.Favorites.as_view(), name='favorites'),
  path('favorites/add/<int:restaurant_id>/', views.add_favorite, name='add_favorite'),
  path('restaurants/<int:restaurant_id>/', views.detailsview, name='detail'),
  path('review/create/', views.ReviewCreate.as_view(), name='review_create'),
  path('review/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
]