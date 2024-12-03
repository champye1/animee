from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise ValidationError("El nombre de usuario debe tener al menos 4 caracteres")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        if not any(char.isdigit() for char in password):
            raise ValidationError("La contraseña debe contener al menos un número")
        if not any(char.isupper() for char in password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula")
        if not any(char.islower() for char in password):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial (!@#$%^&*()_+-=[]{}|;:,.<>?)")
        return password 