import datetime
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria=models.CharField(max_length=50, blank=True, verbose_name="Nombre de categoria")


    def __str__(self):
        return self.nombreCategoria
    
class Animal(models.Model):
    numero = models.CharField(primary_key=True, max_length=10, verbose_name="Id")
    animal = models.CharField(max_length=100, blank=False, verbose_name="Animal")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, verbose_name="Precio")
    visualizaciones = models.PositiveIntegerField(default='', blank=False, verbose_name="Visualizaciones")
    descripcion = models.TextField(max_length=50, null=True)
    imagen=models.ImageField(upload_to="imagenes",null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.numero
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Animal', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)    
