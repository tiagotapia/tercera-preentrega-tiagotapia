from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',home,name="home"),
    path('acercademi',acercaMI,name="acercademi"),
#________________________________________________________________________ agencias
  path('Agencias',agenciaslist.as_view(),name="Agencias"),
   path('Agenciascreate',agenciascreate.as_view(),name="Agenciascreate"),
  path('Agenciasupdate/<int:pk>/',agenciasUpdate.as_view(),name="Agenciasupdate"),
  path('Agenciasdelete/<int:pk>/',agenciasDelete.as_view(),name="Agenciasdelete"),

#_________________________________________________________________________________
 
#__________________________________________________________________________metodo para buscar alguna coincidencia
    path('buscar/',buscar,name="buscar"),
    path('buscarAutoS/',buscarAutoS,name="buscarAutoS"),

#__________________________________________________________________________metodo  para crear agregar y eliminar autos 
    path('autos_disponibles',autos_disponibleslist.as_view(),name="autos_disponibles"),
   path('autos_disponiblescreate',autos_disponiblescreate.as_view(),name="autos_disponiblescreate"),
  path('autos_disponiblesUpdate/<int:pk>/',autos_disponiblesUpdate.as_view(),name="autos_disponiblesUpdate"),
  path('autos_disponiblesDelete/<int:pk>/',autos_disponiblesDelete.as_view(),name="autos_disponiblesDelete"),


#__________________________________________________________________________permutacion
    path('permutacion',permutacionlist.as_view(),name="permutacion"),
   path('permutacioncreate', permutacioncreate.as_view(),name="permutacioncreate"),
  path('permutacionUpdate/<int:pk>/',permutacionUpdate.as_view(),name="permutacionUpdate"),
  path('permutacionDelete/<int:pk>/',permutacionDelete.as_view(),name="permutacionDelete"),


#__________________________________________________________________________metodo de pagoo
  path('metodo_pago',metodo_pagolist.as_view(),name="metodo_pago"),
   path('metodo_pagocreate', metodo_pagocreate.as_view(),name="metodo_pagocreate"),
  path('metodo_pagoUpdate/<int:pk>/',metodo_pagoUpdate.as_view(),name="metodo_pagoUpdate"),
  path(' metodo_pagoDelete/<int:pk>/',metodo_pagoDelete.as_view(),name="metodo_pagoDelete"),

#__________________________________________________________________________mlogin,logout,registro

path('logout/', custom_logout, name="logout"),
path('login/', login_request, name="login"),
path('registro/',register,name="registro"),

path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
path('editar_perfil/', editarPerfil, name="editar_perfil"),
path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
#______________________________________________________________________________ clases 






]

