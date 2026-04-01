from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Estudiante, Asistencia
from .forms import EstudianteForm
from django.utils import timezone


def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required
def estudiantes(request):
    lista = Estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes': lista})

@login_required
def crear(request):
    formulario = EstudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    formulario = EstudianteForm(request.POST or None, request.FILES or None, instance=estudiante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('estudiantes')

@login_required
def detalle(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})

# La vista de almuerzo NO requiere login para uso desde un quiosco/tablet
def almuerzo(request):
    mensaje = None
    contador = None
    nombre = None
    foto_url = None

    if request.method == 'POST':
        documento = request.POST.get('documento')
        try:
            estudiante = Estudiante.objects.get(documento=documento)
            Asistencia.objects.create(estudiante=estudiante, tipo='ALM')
            hoy = timezone.localdate()
            contador = Asistencia.objects.filter(estudiante=estudiante, fecha=hoy, tipo='ALM').count()
            nombre = f"{estudiante.nombres} {estudiante.apellidos}"
            foto_url = estudiante.foto.url if estudiante.foto else None
            mensaje = f"Almuerzos registrados hoy: {contador}"
        except Estudiante.DoesNotExist:
            mensaje = "Documento no encontrado"

    return render(request, 'almuerzo.html', {
        'mensaje': mensaje,
        'contador': contador,
        'nombre': nombre,
        'foto_url': foto_url,
    })
