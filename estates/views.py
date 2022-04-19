from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Propiedad, Publicacion

def index(request):
	propiedades = Propiedad.objects.all()
	publicaciones = Publicacion.objects.all()

	context = {
		'propiedades': propiedades,
		'publicaciones': publicaciones,
	}

	return render(request, 'estates/index.html', context)

def about(request):
	return render(request, 'estates/about.html')

def properties(request):
	propiedades = Propiedad.objects.all()

	context = {
		'propiedades': propiedades,
	}

	return render(request, 'estates/properties.html', context)

def single_propety(request, id):
	propiedad = get_object_or_404(Propiedad, pk=id)

	context = {
		'propiedad': propiedad
	}

	return render(request, 'estates/single-property.html', context)

def blog(request):
	publicaciones = Publicacion.objects.all()

	context = {
		'publicaciones': publicaciones,
	}

	return render(request, 'estates/blog.html', context)

def single_blog(request, id):
	publicacion = get_object_or_404(Publicacion, pk=id)

	context = {
		'publicacion': publicacion,
	}

	return render(request, 'estates/single-blog.html', context)

def contact(request):
	return render(request, 'estates/contact.html')