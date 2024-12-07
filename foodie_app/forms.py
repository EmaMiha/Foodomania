# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Recipe,Diet,Category,Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'ingredients', 'diet', 'categories','image']  
        diet = forms.ModelChoiceField(queryset=Diet.objects.all(), empty_label="Select Diet")
        categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
        ingredients=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':40}))
        instructions=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':40}))

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']


class DietForm(forms.ModelForm):
    class Meta:
        model=Diet
        fields=['name','description']