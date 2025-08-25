from django.http import HttpResponse

def inicio(request):
    nombre = "Ignacio Navarrrete"
    return HttpResponse(f"¡Bienvenido a mi primera app de django, {nombre}!")