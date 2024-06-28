from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Encabezado(models.Model):
    titulo = models.CharField(max_length = 200)
    subtitulo = models.CharField(max_length = 200)
    fondo = models.ImageField(upload_to = 'imagenes', null = True, blank = True)
    def _str_(self):
        return self.titulo + ' - ' + self.subtitulo

class Bienvenida(models.Model):
    saludo = models.CharField(max_length=300)
    texto = models.CharField(max_length=700)
    def _str_(self):
        return self.saludo + ' - ' + self.texto

class HotelesUnaEstrella(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    servicios = models.CharField(max_length=400)
    politica = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre

class HotelesDosEstrellas(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    servicios = models.CharField(max_length=400)
    politica = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre

class HotelesTresEstrellas(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    servicios = models.CharField(max_length=400)
    politica = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre
    
class HotelesCuatroEstrellas(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    servicios = models.CharField(max_length=400)
    politica = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre
    
class HotelesCincoEstrellas(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    servicios = models.CharField(max_length=400)
    politica = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    hotel_una_estrella = models.ForeignKey(HotelesUnaEstrella, on_delete=models.CASCADE, null=True, blank=True)
    hotel_dos_estrellas = models.ForeignKey(HotelesDosEstrellas, on_delete=models.CASCADE, null=True, blank=True)
    hotel_tres_estrellas = models.ForeignKey(HotelesTresEstrellas, on_delete=models.CASCADE, null=True, blank=True)
    hotel_cuatro_estrellas = models.ForeignKey(HotelesCuatroEstrellas, on_delete=models.CASCADE, null=True, blank=True)
    hotel_cinco_estrellas = models.ForeignKey(HotelesCincoEstrellas, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fechaLlegada = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_hotel().nombre}"

    def get_hotel(self):
        if self.hotel_una_estrella:
            return self.hotel_una_estrella
        if self.hotel_dos_estrellas:
            return self.hotel_dos_estrellas
        if self.hotel_tres_estrellas:
            return self.hotel_tres_estrellas
        if self.hotel_cuatro_estrellas:
            return self.hotel_cuatro_estrellas
        if self.hotel_cinco_estrellas:
            return self.hotel_cinco_estrellas
        return None
