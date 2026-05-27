from django.shortcuts import render
from django.http import HttpResponse #HttpResponse sirve para enviar una respuesta HTTP al navegador desde una vista (views.py).

# Create your views here.
def inicio(request): #request es la solicitud a la aplicación
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')
#busca el archivo .html, accede directamente a templates, pero como esta dentro de otra carpeta,
# se direcciona /

def hojas(request):
    return render(request, 'hojas/index.html')

def crearh(request):
    return render(request, 'hojas/crearh.html')

    