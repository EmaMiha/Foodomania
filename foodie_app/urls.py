
# from django.urls import path
# from .views import register, login_view, home

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('login/', login_view, name='login'),
#     path('home/', home, name='home'),
# ]

# # urls.py
# from django.urls import path
# from foodie_app import views as index_views

# urlpatterns = [
#     path('', index_views.login_view, name='login'),  # Redirect root to login
#     path('register/', index_views.register, name='register'),
#     path('home/', index_views.home, name='home'),
# ]



from django.urls import path
from . import views  # Import views
from django.contrib.auth.views import LogoutView  # Import the LogoutView


urlpatterns = [
    path('', views.home, name='home'),  
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path("delete-recipe/<int:recipe_id>/",views.delete_recipe,name="delete_recipe"),
]