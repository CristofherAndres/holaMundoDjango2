from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def despedir(request):
    return HttpResponse("<h1>Chao Mundo 🥲</h1>")