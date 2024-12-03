from django.core.management.base import BaseCommand
from gallery.models import Galeria
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Carga datos de ejemplo en la galería'

    def handle(self, *args, **kwargs):
        personajes = [
            {
                'title': 'Ahri',
                'description': 'La Zorra de Nueve Colas',
                'linea': 'Mid',
                'tipo': 'Mago',
                'imagen_nombre': 'ahri.jpg'
            },
            {
                'title': 'Darius',
                'description': 'La Mano de Noxus',
                'linea': 'Top',
                'tipo': 'Tanque',
                'imagen_nombre': 'darius.jpg'
            },
            # Agrega más personajes aquí
        ]

        # Directorio donde están las imágenes de ejemplo
        img_dir = os.path.join(settings.BASE_DIR, 'gallery', 'sample_images')
        
        for personaje in personajes:
            galeria, created = Galeria.objects.get_or_create(
                title=personaje['title'],
                defaults={
                    'description': personaje['description'],
                    'linea': personaje['linea'],
                    'tipo': personaje['tipo']
                }
            )
            
            # Intentar cargar la imagen si existe
            imagen_path = os.path.join(img_dir, personaje['imagen_nombre'])
            if os.path.exists(imagen_path):
                with open(imagen_path, 'rb') as img_file:
                    galeria.imagen.save(
                        personaje['imagen_nombre'],
                        File(img_file),
                        save=True
                    )
            
            self.stdout.write(
                self.style.SUCCESS(f'{"Creado" if created else "Actualizado"} personaje: {personaje["title"]}')
            )