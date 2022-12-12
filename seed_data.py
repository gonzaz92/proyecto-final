from ejemplo.models import Familiar, Juegos

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

Juegos(nombre='Megaman', tipo= 'Plataformas')
Juegos(nombre='Zelda, Ocarina Of time', tipo= 'Aventura')
Juegos(nombre='Golden Sun', tipo= 'Rol')

print("Se cargo con éxito los usuarios de pruebas")