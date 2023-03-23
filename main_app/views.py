from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Review, Favorite
from googlemaps import Client as cl
from django.urls import reverse
import os
import environ

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # creates empty instance of a signup form
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      #Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - please try again!'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RestaurantList(ListView):
  model = Restaurant

class RestaurantCreate(CreateView):
  model = Restaurant
  fields = ['name', 'description', 'category']

def CategoryList(request):
  g_api = os.environ['GOOGLE_MAP']
  gmaps = cl(key= g_api)
  restaurants = gmaps.places_nearby(location='34.020479,-118.4117325', radius=500, type='restaurant')
  context = {'restaurants': restaurants}
  return render(request, 'restaurants/categories.html', {'context': context, 'g_api': g_api})
#  return render(request, 'restaurants/categories.html')
  
def detailsview(request, restaurant_id):
  reviews = Review.objects.filter(restaurant=restaurant_id)
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurants/detail.html', {
  'reviews' : reviews,
  'restaurant': restaurant,
  'user': request.user
})

class Favorites(LoginRequiredMixin, ListView):
  model = Favorite

class ReviewCreate(LoginRequiredMixin, CreateView):
  model = Review
  fields = ['title', 'description', 'restaurant']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    review = form.save()
    id = review.restaurant.id
    url = reverse('detail', args=[id])
    return redirect(url)

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  fields = ['title', 'description']
  def get_success_url(self):
    return reverse('detail', args=[self.object.restaurant.id])