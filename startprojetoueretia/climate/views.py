

from django.shortcuts import render

from django.http import HttpResponse


def climate(request):
    return render(request, 'clima.html')


def tips(request):
    return render(request, 'dicas.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registrar.html')

# Create your views here.
from django.shortcuts import render