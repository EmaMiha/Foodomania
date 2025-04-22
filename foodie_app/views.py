from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import CategoryForm, DietForm
from .models import Recipe, Comment, Category, Diet, Ingredient, Instructions
from .forms import RecipeForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse


def index(request):
    return render(request, "login.html")


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def add_diet(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DietForm()

    return render(request, 'add_diet.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}! 🎉')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Invalid data')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    try:
        search_query = request.GET.get('search',  '')
        recipes = Recipe.objects.filter(title__icontains=search_query)
        selected_diets = request.GET.getlist('diets')
        selected_categories = request.GET.getlist('categories')

        if selected_diets:
            recipes = recipes.filter(diet__id__in=selected_diets).distinct()

        if selected_categories:
            recipes = recipes.filter(
                categories__id__in=selected_categories).distinct()

        paginator = Paginator(recipes, 6)
        page_number = request.GET.get('page')
        recipess = paginator.get_page(page_number)

        diets = Diet.objects.all()
        categories = Category.objects.all()

        return render(
            request,
            'home.html',
            {
                'recipes': recipess,
                'search_query': search_query,
                'diets': diets,
                'categories': categories,
                'selected_categories': selected_categories,
                'selected_diets': selected_diets})
    except Exception as e:
        import traceback
        print("❌ ERROR in home view:", e)
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        ingredients = request.POST.getlist('ingredients[]')
        instructions = request.POST.getlist('instructions[]')
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for ingredient_name in ingredients:
                if ingredient_name.strip():
                    Ingredient.objects.create(
                        recipe=recipe, name=ingredient_name.strip())
            for index, inst in enumerate(instructions, start=1):
                if inst.strip():
                    Instructions.objects.create(
                        recipe=recipe, step_number=index, description=inst)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True,
                                     'message': 'Recipe successfully added!'})
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False,
                                     'message': 'Failed to add recipe.'})
    else:
        form = RecipeForm()

    return render(request, 'add_recipe.html', {'form': form})


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author or request.user.is_superuser:
        recipe.delete()
    return redirect('home')


@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    ingredients = recipe.ingredients.all()
    instructions = recipe.instructions.all()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        new_ingredients = request.POST.getlist('ingredients[]')
        new_instructions = request.POST.getlist('instructions[]')

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            Ingredient.objects.filter(recipe=recipe).delete()
            for item in new_ingredients:
                Ingredient.objects.create(recipe=recipe, name=item.strip())

            Instructions.objects.filter(recipe=recipe).delete()
            for index, step in enumerate(new_instructions, start=1):
                Instructions.objects.create(
                    recipe=recipe, step_number=index, description=step)

        return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request,
                  "update_recipe.html",
                  {
                      'form': form,
                      'recipe': recipe,
                      'ingredients': ingredients,
                      'instructions': instructions})


@login_required
def add_comment(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        comment = Comment(recipe=recipe, author=request.user, content=content)

        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)
            comment.parent = parent_comment
        comment.save()
        messages.success(request, "Comment successfully added! ✅")
        return redirect('home')


@login_required
def delete_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author or request.user.is_superuser:

        comment.replies.all().delete()
        comment.delete()
        messages.success(request, "Comment successfully deleted! 🗑️")
    return redirect('home')


@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user not in recipe.likes.all():
        recipe.likes.add(request.user)
    else:
        recipe.likes.remove(request.user)

    return JsonResponse(
        {
            'likes_count': recipe.number_of_likes(),
            'liked': request.user in recipe.likes.all()})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients_list = recipe.ingredients.all()
    instructions_list = recipe.instructions.all()
    return render(request, 'recipe_detail.html',
                  {
                      'recipe': recipe,
                      'ingredients': ingredients_list,
                      'instructions': instructions_list})


def about(request):
    return render(request, 'about.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out. See you again!")
    return redirect('home')
