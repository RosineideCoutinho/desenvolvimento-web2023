
from django.shortcuts import render

from django.http import HttpResponse


def climate(request):
    return HttpResponse('clima.html')


def tips(request):
    return HttpResponse('dicas.html')


def users(request):
    return HttpResponse('login.html')

def register(request):
    return HttpResponse('registrar.html')

# Create your views here.
from django.shortcuts import render

# Create your views here.
