
from django.shortcuts import render

from django.http import HttpResponse


def clima(request):
    return HttpResponse('clima.html')


def dicas(request):
    return HttpResponse('dicas.html')


def login(request):
    return HttpResponse('login.html')

def registrar (request):
    return HttpResponse('registrar.html')

# Create your views here.
from django.shortcuts import render

# Create your views here.
