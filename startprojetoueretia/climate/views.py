

from django.shortcuts import render

from django.http import HttpResponse


def climate(request):
    return render(request, 'clima.html')



