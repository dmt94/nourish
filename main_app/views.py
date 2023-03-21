from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Restaurant, Review
from googlemaps import Client as cl


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

class CategoryList(ListView):
  template_name = 'main_app/restaurant_categories.html'

  def get_queryset(self):
    self.category = get_object_or_404(Restaurant, name=self.kwargs['category'])
    return Restaurant.objects.filter(category=self.category)
  
def detailsview(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurants/detail.html', {
  'restaurant': restaurant
})

