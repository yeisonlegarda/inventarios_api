from django.db import models

# Create your models here.
class Tipo_producto(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=250,null=True)

    def __str__(self):
        return '{}'.format("Informacion tipos productos")

    class Meta:
        verbose_name_plural = "Tipos_Productos"

class Estado(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=250,null=True)

    def __str__(self):
        return '{}'.format("Informacion estados de productos")

    class Meta:
        verbose_name_plural = "Estados"

class Responsable(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format("Informacion Responsables")
    class Meta:
        verbose_name_plural = "Responsables"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50,null=True)
    tipo = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    serialnb = models.CharField(max_length=50,)
    estado_actual = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    responsable = models.ForeignKey(Responsable, on_delete=models.DO_NOTHING)
    fecha_compra = models.DateField()
    valor_compra = models.FloatField()

    def __str__(self):
        return '{}'.format("Informacion productos")

    class Meta:
        verbose_name_plural = "productos"

class Persona(Responsable):
    cedula = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format("Informacion personas que tienen a cargo productos")

    class Meta:
        verbose_name_plural = "personas"

class Area(Responsable):
    abreviacion = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format("Informacion areas")

    class Meta:
        verbose_name_plural = "areas"
