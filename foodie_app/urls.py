
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path("delete-recipe/<int:recipe_id>/", views.delete_recipe,
         name="delete_recipe"
         ),
    path("update-recipe/<int:recipe_id>/", views.update_recipe,
         name="update_recipe"
         ),
    path("add-comment/<int:recipe_id>/",
         views.add_comment, name="add_comment"),
    path("delete-comment/<int:comment_id>/",
         views.delete_comment, name="delete_comment"
         ),
    path("add-category/", views.add_category, name="add_category"
         ),
    path("add-diet/", views.add_diet, name="add_diet"),
    path('like-recipe/<int:recipe_id>/', views.like_recipe,
         name="like_recipe"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('about/', views.about, name='about'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
