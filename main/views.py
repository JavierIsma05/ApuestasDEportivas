from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.profile_image = request.FILES.get('profile_image', profile.profile_image)
        profile.user.username = request.POST.get('username', profile.user.username)
        profile.user.email = request.POST.get('email', profile.user.email)
        profile.user.save()
        profile.save()
        return redirect('profile')  # Redirigir a la página del perfil

    return render(request, 'profile/edit_profile.html')


@login_required
def matches(request):
    return render(request, 'app/matches.html')

@login_required
def editions(request):
    if request.user.role == 'admin':
        return render(request, 'app/editions.html')
    return render(request, 'main/403.html')  # Página de acceso denegado

@login_required
def creation(request):
    if request.user.role in ['admin', 'editor']:
        return render(request, 'main/creation.html')
    return render(request, 'main/403.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Cambia a la ruta que prefieras

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib import messages
from .forms import AdminUserCreationForm, UserCreationForm

# Verifica si el usuario es administrador
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

# Vista para registro de usuarios comunes
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'  # El rol predeterminado para usuarios normales
            user.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
# Vista para registro por administradores
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AdminUserCreationForm

@login_required
def admin_register(request):
    if request.user.role != 'admin':  # Restringir acceso solo a administradores
        return render(request, 'main/403.html')  # Página de acceso denegado
    
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('admin_register')
    else:
        form = AdminUserCreationForm()
    
    return render(request, 'registration/admin_register.html', {'form': form})
