from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('autos_disponibles',ver_autos_disponibles,name="autos_disponibles"),
    path('metodo_pago',ver_metodo_pago,name="metodo_pago"),
    path('permutacion',ver_permutacion,name="permutacion"),
#
    path('autos_form/',ver_autosform,name="autos-form"),
    path('metodo_pagoform/',ver_metodo_pagoform,name="metodo_pago-form"),
    path('permutacionform/',ver_permutacionform,name="permutacion-form"),

    path('buscar/',buscar,name="buscar"),
    path('buscarAutoS/',buscarAutoS,name="buscarAutoS"),
]

