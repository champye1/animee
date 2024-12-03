from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Galeria, Comentario
from .forms import ComentarioForm

def galeria(request):
    linea_filtro = request.GET.get('linea')
    tipo_filtro = request.GET.get('tipo')
    
    galerias = Galeria.objects.all()
    
    if linea_filtro and linea_filtro != 'Todas las lineas':
        galerias = galerias.filter(linea=linea_filtro)
    if tipo_filtro and tipo_filtro != 'Todos los tipos':
        galerias = galerias.filter(tipo=tipo_filtro)
    
    context = {
        'galerias': galerias,
        'lineas': Galeria.LINEA_CHOICES,
        'tipos': Galeria.TIPO_CHOICES,
        'comentario_form': ComentarioForm(),
        'linea_actual': linea_filtro,
        'tipo_actual': tipo_filtro,
    }
    return render(request, 'gallery/galeria.html', context)

@login_required
def agregar_comentario(request, galeria_id):
    if request.method == 'POST':
        galeria = get_object_or_404(Galeria, id=galeria_id)
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(
                usuario=request.user,
                galeria=galeria,
                texto=texto
            )
            messages.success(request, 'Comentario agregado exitosamente.')
    return redirect('gallery:galeria')




