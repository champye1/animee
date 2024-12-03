from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from perfil.models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ahora puedes iniciar sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
