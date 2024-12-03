from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
] 