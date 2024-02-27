from django.shortcuts  import render,redirect
from django.http       import HttpResponse 
from django.urls       import reverse_lazy



from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView





from django.contrib.auth.forms       import AuthenticationForm
from django.contrib.auth             import authenticate, login,logout
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins      import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,"aplicacion/home.html")
def acercaMI(request):
     return render(request,"aplicacion/acercademi.html")
#________________________________________________________- agencias
class agenciaslist(LoginRequiredMixin,ListView):
     model=agencias
class agenciascreate(LoginRequiredMixin,CreateView):
     model=agencias
     fields=["nombre_agencias","nombre_dueño","direccion","image"]
     success_url=reverse_lazy("Agencias")
class agenciasUpdate(LoginRequiredMixin,UpdateView):
      model=agencias
      fields=["nombre_agencias","nombre_dueño","direccion","image"]
      success_url=reverse_lazy("Agencias")
class agenciasDelete(LoginRequiredMixin,DeleteView):
      model=agencias
      success_url=reverse_lazy("Agencias")

#____________________________________________________________________

class autos_disponibleslist(LoginRequiredMixin,ListView):
     model=autos_disponibles
class autos_disponiblescreate(LoginRequiredMixin,CreateView):
     model=autos_disponibles
     fields=["nombre_auto","nombre_primer_dueño","email","modelo","imagen"]
     success_url=reverse_lazy("autos_disponibles")
class autos_disponiblesUpdate(LoginRequiredMixin,UpdateView):
      model=autos_disponibles
      fields=["nombre_auto","nombre_primer_dueño","email","modelo","imagen"]
      success_url=reverse_lazy("autos_disponibles")
class autos_disponiblesDelete(LoginRequiredMixin,DeleteView):
      model=autos_disponibles
      success_url=reverse_lazy("autos_disponibles")

#____________________________________________________________________________

class permutacionlist(LoginRequiredMixin,ListView):
     model=permutacion
class permutacioncreate(LoginRequiredMixin,CreateView):
     model=permutacion
     fields=["nombre_auto","nombre_primer_dueño","email","modelo","imagenes"]
     success_url=reverse_lazy("permutacion")
class permutacionUpdate(UpdateView):
      model=permutacion
      fields=["nombre_auto","nombre_primer_dueño","email","modelo","imagenes"]
      success_url=reverse_lazy("permutacion")
class permutacionDelete(LoginRequiredMixin,DeleteView):
      model=permutacion
      success_url=reverse_lazy("permutacion")
#_____________________________________________________________________________________
class metodo_pagolist(LoginRequiredMixin,ListView):
     model=metodo_pago
class metodo_pagocreate(LoginRequiredMixin,CreateView):
     model=metodo_pago
     fields=["efectivo"]
     success_url=reverse_lazy("metodo_pago")
class metodo_pagoUpdate(LoginRequiredMixin,UpdateView):
      model=metodo_pago
      fields=["efectivo"]
      success_url=reverse_lazy("metodo_pago")
class metodo_pagoDelete(LoginRequiredMixin,DeleteView):
      model=metodo_pago
      success_url=reverse_lazy("metodo_pago")

#____________________________________________________________________________
# buscando coincidencias 

def buscar(request):
   return render(request,"aplicacion/buscar.html")

def buscarAutoS(request):
     if request.GET["buscar"]:
          patron=request.GET["buscar"]
          autos=autos_disponibles.objects.filter( nombre_auto__icontains=patron)
          contexto={"autos_disponibles":autos}
          return render(request,"aplicacion/autos_disponibles.html",contexto)
     return HttpResponse("no se ingresaron patrones de busquedas")
#___________________________________________________________________________
#________________________________________________ login,logout,registracion
def custom_logout(request):
     logout(request)
     return redirect(reverse_lazy('home'))

def login_request(request):
     if request.method == "POST":
          usuario=request.POST['username']
          password=request.POST['password']
          user=authenticate(request,username=usuario,password=password)
          if user is not None:
               login(request,user)

               #___ avatar del usuario
               try:
                    avatar=Avatar.objects.get(user=request.user.id).imagen.url
               except:
                    avatar="/media/avatares/default.png"
               finally:
                    request.session["avatar"]=avatar
               #_________________________________


               return render(request,"aplicacion/home.html")
          else:
               return redirect(reverse_lazy,('login'))
     miform=AuthenticationForm()     
     return render(request,"aplicacion/login.html",{"form":miform})
def register(request):
    if request.method == "POST":
        miForm =registroform(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm =registroform()

    return render(request, "aplicacion/registro.html", {"form": miForm })  
           

#_____________________________________________________________ modificacion de usuario
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarperfil.html", {"form": form }) 

@login_required
def agregarAvatar(request):
     if request.method=="POST":
          form= avatarform(request.POST, request.FILES)
          if form.is_valid():
               usuario=User.objects.get(username=request.user)
               #___borrar avatar viejo
               avatarViejo=Avatar.objects.filter(user=usuario)
               if len(avatarViejo)>0:
                    for i in range(len(avatarViejo)):
                         avatarViejo[i].delete()
                 #________________________________
               avatar=Avatar(user=usuario,imagen=form.cleaned_data["imagen"])
               avatar.save()
               #_____________________ hago una url de la imagen en request
               imagen=Avatar.objects.get(user=request.user.id).imagen.url
               request.session["avatar"]=imagen
               return render(request,"aplicacion/home.html")
                              

     else:
          form=avatarform()
     return render(request,"aplicacion/agregarAvatar.html",{"form":form})

               
