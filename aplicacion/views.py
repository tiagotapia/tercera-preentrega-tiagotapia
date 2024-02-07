from django.shortcuts import render
from django.http import HttpResponse 



from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request,"aplicacion/home.html")

def ver_autos_disponibles(request):
     contexto={'autos_disponibles': autos_disponibles.objects.all()}
     return render(request,"aplicacion/autos_disponibles.html",contexto)

def ver_autosform(request):
     if request.method == "POST":
          miform=autosform(request.POST)
          if miform.is_valid():
               a=miform.cleaned_data.get("nombre_auto")
               e=miform.cleaned_data.get("dueño")
               c=miform.cleaned_data.get("modelo")
               d=miform.cleaned_data.get("correo")
               
               auto=autos_disponibles(nombre_auto=a,nombre_primer_dueño=e,modelo=c,email=d)
               
               auto.save()
               return render (request,'aplicacion/home.html')
     
     else:
          miform=autosform()
     
     return render(request,"aplicacion/autosform.html",{"form":miform})

def ver_metodo_pago(request):
     contexto={'metodo_pago': metodo_pago.objects.all()}
     return render(request,"aplicacion/metodo_pago.html",contexto)
def ver_metodo_pagoform(request):
     if request.method == "POST":
          miform=metodo_pagoform(request.POST)
          if miform.is_valid():
               a=miform.cleaned_data.get("efectivo")
               pago=metodo_pago(efectivo=a)
               pago.save()
               return render (request,'aplicacion/home.html')
     else:
          miform=autosform()
     return render(request,"aplicacion/metodo_pagoform.html",{"form":miform})






def ver_permutacion(request):
     contexto={'permutacion': permutacion.objects.all()}
     return render(request,"aplicacion/permutacion.html",contexto)

def ver_permutacionform(request):
     if request.method == "POST":
          miform=permutacionform(request.POST)
          if miform.is_valid():
               a=miform.cleaned_data.get("nombre_autoo")
               e=miform.cleaned_data.get("nombre_primer_dueñoo")
               c=miform.cleaned_data.get("modeloo")
               d=miform.cleaned_data.get("emaill")
               
               permutar=permutacion(nombre_auto=a,nombre_primer_dueño=e,modelo=c,email=d)
               
               permutar.save()
               return render (request,'aplicacion/home.html')
     
     else:
          miform=permutacionform()
     
     return render(request,"aplicacion/permutacionform.html",{"form":miform})

def buscar(request):
     return render(request,"aplicacion/buscar.html")
def buscarAutoS(request):
     if request.GET["buscar"]:
          patron=request.GET["buscar"]
          autos=autos_disponibles.objects.filter( nombre_auto__icontains=patron)
          contexto={"autos_disponibles":autos}
          return render(request,"aplicacion/autos_disponibles.html",contexto)
     return HttpResponse("no se ingresaron patrones de busquedas")

