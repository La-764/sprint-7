
from django.shortcuts import render, HttpResponse
# Create your views here.

def login(request):
    return render(request, "webitbank/Login.html")

def home(request):
    
    return render(request, "webitbank/index.html")

def pagoServicios(request):
    return render(request, "webitbank/pago_servicios.html")
         

def productos(request):
    return render(request, "webitbank/pages/productos.html")

def dolar(request):
    return render(request, "webitbank/pages/dolar.html")

def noticias(request):
    return render(request, "webitbank/pages/noticias.html")

def prestamos(request):
    return render(request, "webitbank/pages/prestamos.html")

def transferencias(request):
    return render(request, "webitbank/pages/transferencias.html")

def turnos(request):
    return render(request, "webitbank/pages/turnos.html")
    
def seguros(request):
    return render(request, "webitbank/pages/seguros.html")