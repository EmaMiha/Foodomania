from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Recipe,Comment
from .forms import RecipeForm 
from django.shortcuts import get_object_or_404

def index(request):
    return render(request,"login.html")


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

def home(request):
    recipes = Recipe.objects.all()  # Fetch all posts (recipes)
    return render(request, 'home.html', {'recipes': recipes, 'user':request.user})



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

def delete_recipe(request,recipe_id):
    if request.method=='POST':
        recipe=get_object_or_404(Recipe,id=recipe_id,author=request.user)
        recipe.delete()
        return redirect('home')
    else:
        return redirect('home')


def update_recipe(request, recipe_id):
    recipe=get_object_or_404(Recipe,id=recipe_id,author=request.user)
    if request.method=='POST':
        form=RecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=RecipeForm(instance=recipe)
    
    return render(request,"update_recipe.html",{'form':form,'recipe':recipe})


def add_comment(request,recipe_id):
    if request.method=='POST':
        recipe=get_object_or_404(Recipe,id=recipe_id)
        content=request.POST.get('content')
        parent_id=request.POST.get('parent_id')
        comment=Comment(recipe=recipe,author=request.user,content=content)
        
        if parent_id:
            parent_comment=get_object_or_404(Comment,id=parent_id)
            comment.parent=parent_comment
        comment.save()
        return redirect('home')
    



def delete_comment(request,comment_id):

    comment=get_object_or_404(Comment,id=comment_id,author=request.user)
    comment.replies.all().delete()
    comment.delete()
        
        
    return redirect('home')
    

