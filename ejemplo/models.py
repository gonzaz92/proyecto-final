from django.db import models
from datetime import datetime

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Mascota(models.Model):
  nombre: models.CharField(max_length=30)
  especie: models.CharField(max_length=30)
  raza: models.CharField(max_length=30)

  def __str__(self):
    return f'{self.nombre}, {self.especie}, {self.raza}, {self.id}'

class Juegos(models.Model):
  nombre = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.nombre}, {self.tipo}, {self.id}'