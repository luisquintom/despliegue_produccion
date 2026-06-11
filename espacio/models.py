from django.db import models

# Create your models here.

class Agencia(models.Model):
    nombre = models.CharField(max_length=100)  
    pais = models.CharField(max_length=100)   

    def __str__(self):
        return self.nombre

class Mision(models.Model):
    nombre_clave = models.CharField(max_length=100) 
    destino = models.CharField(max_length=100)      
    coste_lanzamiento = models.DecimalField(max_digits=10, decimal_places=2) # En millones

    # Si se borra la agencia, se borran sus misiones (CASCADE)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE, related_name='misiones')

    def __str__(self):
        return self.nombre_clave