from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#________________________________________________ modelo de autos
class autos_disponibles(models.Model):
    nombre_auto=models.CharField(max_length=50)
    nombre_primer_dueño=models.CharField(max_length=50,null=False)
    email=models.EmailField()
    modelo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="avatares",blank=True,null=True)
#_____________________________________________________________________
    

#_________________________________________________________________ modelo de metodo de pago
class metodo_pago(models.Model):
     efectivo=models.CharField(max_length=50)
 #___________________________________________________________________________



#_____________________________________________________________________modelo de permutacion         
class permutacion(models.Model):
     nombre_auto=models.CharField(max_length=50)
     nombre_primer_dueño =models.CharField(max_length=50)
     email=models.EmailField()
     modelo =models.IntegerField()
     imagenes=models.ImageField(upload_to="avatares",blank=True,null=True)
     def  __str__(self):
          return f"{self.nombre_auto}"
#_____________________________________________________________________________________modelo de avatar
     
class Avatar(models.Model):
     imagen=models.ImageField(upload_to="avatares")
     user=models.ForeignKey(User,on_delete=models.CASCADE)

     def __str__(self):
          return f"{self.user} {self.imagen}"
#____________________________________________________________________________________________________________


 #______________________________________________________________________________modelo de agencias    
class agencias(models.Model):
     nombre_agencias=models.CharField(max_length=50)
     nombre_dueño=models.CharField(max_length=50)
     direccion=models.CharField(max_length=50)
     image=models.ImageField(upload_to="avatares",blank=True,null=True)

#_________________________________________________________________________________________________________________
 
    