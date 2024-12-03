from django.db import models
from django.contrib.auth.models import User

class Galeria(models.Model):
    LINEA_CHOICES = [
        ('Top', 'Top'),
        ('Mid', 'Mid'),
        ('ADC', 'ADC'),
        ('Support', 'Support'),
        ('Jungle', 'Jungle'),
    ]
    
    TIPO_CHOICES = [
        ('Asesino', 'Asesino'),
        ('Tanque', 'Tanque'),
        ('Mago', 'Mago'),
        ('Tirador', 'Tirador'),
        ('Soporte', 'Soporte'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to='galeria/')
    linea = models.CharField(max_length=10, choices=LINEA_CHOICES, default='Top')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='Asesino')
    
    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'
    
    def __str__(self):
        return f"{self.title} - {self.get_linea_display()} - {self.get_tipo_display()}"

    def get_imagen_url(self):
        return self.imagen.url if self.imagen else '/static/gallery/img/default.jpg'

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.galeria.title}'

