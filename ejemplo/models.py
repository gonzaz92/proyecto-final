from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Juegos(models.Model):
  nombre = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.nombre}, {self.tipo}, {self.id}'
  
class Mascotas(models.Model):
  nombre = models.CharField(max_length=50)
  especie = models.CharField(max_length=50)
  raza = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.nombre}, {self.especie}, {self.raza}, {self.id}'