from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
ESTADO_CHOICES = [
        ('OLD', 'Usado'),
        ('NEW', 'Nuevo'),
    ]
TIPO_CHOICES = [
        ('AU', 'Auto'),
        ('MO', 'Moto'),
        ('CA', 'Camion'),
    ]
CAMBIOS_CHOICES = [
        ('AU', 'Automatico'),
        ('MA', 'Manual'),
    ]
COMBUSTIBLE_CHOICES = [
        ('AU', 'Auto'),
        ('MO', 'Moto'),
        ('CA', 'Camion'),
    ]
PUERTAS_CHOICES = [
        ('3', 'Tres Puertas'),
        ('5', 'Cinco Puertas'),
    ]
ASIENTOS_CHOICES = [
        ('2', 'Dos Asientos'),
        ('5', 'Cinco Asientos'),
    ]
class Vehiculo(models.Model):
    nombre = models.CharField(max_length=50)
    fotoPortada = models.ImageField(max_length=100, upload_to='portadas/', blank=True)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    estado = models.CharField(
        max_length=3,
        choices=ESTADO_CHOICES,
    )

    def __str__(self):
        return self.nombre