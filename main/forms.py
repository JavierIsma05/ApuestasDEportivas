from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Formulario para administradores (permite elegir roles)
class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

# Formulario para usuarios comunes (no permite elegir roles)
class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
