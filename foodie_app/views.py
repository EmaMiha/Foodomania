from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
# # Create your views here.

def index(request):
    return render(request,"login.html")


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Recipe  # Assuming Recipe is your post model
from .forms import RecipeForm  # Make sure you create a form for the Recipe model


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('logiin')  # Redirect to a login
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or any other page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    recipes = Recipe.objects.all()  # Fetch all posts (recipes)
    return render(request, 'home.html', {'recipes': recipes})



def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            form.save()  # Save the new recipe to the database
            
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
