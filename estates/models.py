from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# propiedades
class Tipo(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = _('Tipo de propiedad')
		verbose_name_plural = _('Tipo de propiedades')

opciones = [
	[0, "Venta"],
	[1, "Renta"]
]

class Propiedad(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	precio = models.IntegerField()
	opcion = models.IntegerField(choices=opciones)
	ubicacion = models.CharField(max_length=200)
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
	destacado = models.BooleanField()
	portada = models.ImageField(upload_to='covers')
	asesor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = _('Propiedad')
		verbose_name_plural = _('Propiedades')

class Imagen(models.Model):
	nombre = models.ImageField(upload_to='extra')
	propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='imagenes')

	class Meta:
		verbose_name = _('imagen')
		verbose_name_plural = _('Imágenes')

class Detalle(models.Model):
	dimensiones = models.CharField(max_length=200)
	area = models.CharField(max_length=200)
	cuartos = models.IntegerField()
	baños = models.IntegerField()
	garage = models.BooleanField()
	picina = models.BooleanField()
	propiedad = models.OneToOneField(Propiedad, on_delete=models.CASCADE, related_name='detalles')

	class Meta:
		verbose_name = _('Detalles de propiedad')
		verbose_name_plural = _('Detalles de propiedad')
# propiedades

# blog
class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = _('Categoría')
		verbose_name_plural = _('Categorías')

class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
	texto = models.TextField()
	portada = models.ImageField(upload_to='blog')
	fecha = models.DateField()
	autor = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = _('Publicación')
		verbose_name_plural = _('Publicaciones')
# blog

# informacion extra para usuarios
class InformacionExtra(models.Model):
	descripcion = models.TextField()
	telefono = models.CharField(max_length=10)
	facebook = models.CharField(max_length=200, null=True)
	twitter = models.CharField(max_length=200, null=True)
	instagram = models.CharField(max_length=200, null=True)
	linkedin = models.CharField(max_length=200, null=True)
	fotografia = models.ImageField(upload_to='users')
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='informacion')

	class Meta:
		verbose_name = _('Información extra')
		verbose_name_plural = _('Información extra')
# informacion extra para usuarios
