from django import forms

class autosform(forms.Form):
    nombre_auto=forms.CharField(max_length=50,required=True)
    dueño=forms.CharField(max_length=50,required=True)
    correo=forms.EmailField(required=True)
    modelo=forms.CharField(max_length=50,required=True)
class metodo_pagoform(forms.Form):
    efectivo=forms.CharField(max_length=50,required=True)


class permutacionform(forms.Form):
     nombre_autoo=forms.CharField(max_length=50,)
     nombre_primer_dueñoo =forms.CharField(max_length=50,)
     emaill=forms.EmailField()
     modeloo =forms.IntegerField()