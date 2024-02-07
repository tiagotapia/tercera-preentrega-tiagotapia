from django.db import models

# Create your models here.
class autos_disponibles(models.Model):
    nombre_auto=models.CharField(max_length=50)
    nombre_primer_dueño=models.CharField(max_length=50,null=False)
    email=models.EmailField()
    modelo=models.CharField(max_length=50)
    class meta:
        verbose_name="autosdisponible"
        verbose_name_plural="autosdisponible"
    
    def __str__(self):
        return f"{self.nombre_auto}"
    
        


class metodo_pago(models.Model):
     efectivo=models.CharField(max_length=50)
class permutacion(models.Model):
     nombre_auto=models.CharField(max_length=50)
     nombre_primer_dueño =models.CharField(max_length=50)
     email=models.EmailField()
     modelo =models.IntegerField()
     def  __str__(self):
          return f"{self.nombre_auto}"
    