from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.galeria, name='galeria'),
    path('comentario/<int:galeria_id>/', views.agregar_comentario, name='agregar_comentario'),
] 