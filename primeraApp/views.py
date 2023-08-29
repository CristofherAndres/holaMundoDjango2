from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def saludar(request):
    return HttpResponse("<h1>Hola Mundo 🍕</h1>")

def displayFechaHora(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora: </b>" + str(dt)
    return HttpResponse(s)

def renderTemplate(request):
    return render(request, "primerTemplate.html")