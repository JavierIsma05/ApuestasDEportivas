from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('matches/', views.matches, name='matches'),
    path('profile/', views.profile, name='profile'),
    path('editions/', views.editions, name='editions'),
    path('creation/', views.creation, name='creation'),
    
    path('register/', views.user_register, name='user_register'),

    # Ruta para administradores
    path('admin-register/', views.admin_register, name='admin_register'),

]
