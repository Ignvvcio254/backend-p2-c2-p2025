from django.shortcuts import render

def inicio(request):
    nombre = "Ignacio Navarrete"
    context = {
        'nombre': nombre,
    }
    return render(request, 'bienvenida/inicio.html', context)