
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms  import PersonForm
from .models import Person

from django.http import HttpResponse




def users(request):
    return render(request,'login.html')

def home (request):
person= Person.objeto.all()
return render (request, "person_crate.html", ("person":person))



def salvar (request):
Vnome =request.POST.get("nome" )
Person.objeto.create ("nome-vnome")
Person= Person.objects.all()
return render(request, "update.html",("pessoa": person ))

def editar (request, id):
person = Person.objects.get(id=id)
return render(request, "update.html", ("pessoa": person ))

def update (request,id):
vnome= raquest,POST.get("nome")
person= Person.objects.get(id-id)
person= nome= vnome
person.save()
return redirect(home)

def delete (request, id):
person = Person.objects.get(id=id)
return redirect (home)



# Create your views here.
from django.shortcuts import render

# Create your views here.
