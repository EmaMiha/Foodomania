from django.db import models
from django.contrib.auth.models import User

class Diet(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title=models.CharField(max_length=200)
    diet=models.ManyToManyField(Diet,related_name="recipes")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    instructions=models.TextField()
    ingredients=models.TextField()
    categories=models.ManyToManyField(Category,related_name="recipes")
    image=models.ImageField(upload_to="recipes/images/",blank=True,null=True)
    
    def __str__(self):
        return self.title
    def edit_instructions(self,new_instructions):
        self.instructions=new_instructions
        self.save()
    def delete_recipe(self):
        self.delete()

class Comment(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name="comments")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.recipe.title}"
