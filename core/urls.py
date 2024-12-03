from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clasicos/', views.clasicos, name='clasicos'),
    path('actuales/', views.actuales, name='actuales'),
] 