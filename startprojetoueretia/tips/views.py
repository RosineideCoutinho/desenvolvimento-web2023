
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person

# Create your views here.
def start(request):
    #return HttpResponse(
        #"Meu primeiro response html django")
    return render(request, 'test.html')



def climate(request):
    return HttpResponse('clima.html')


def tips(request):
    return HttpResponse('dicas.html')


def login(request):
    return HttpResponse('login.html')

def register(request):
    return HttpResponse('registrar.html')

# Create your views here.
