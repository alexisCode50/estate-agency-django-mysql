from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Propiedad, Publicacion

def index(request):
	propiedades = Propiedad.objects.order_by('?')[:6]
	publicaciones = Publicacion.objects.order_by('?')[:6]

	context = {
		'propiedades': propiedades,
		'publicaciones': publicaciones,
	}

	return render(request, 'estates/index.html', context)

def about(request):
	return render(request, 'estates/about.html')

def properties(request):
	page = request.GET.get('page', 1)
	lista_propiedades = Propiedad.objects.all()

	paginator = Paginator(lista_propiedades, 10)

	try:
		propiedades = paginator.page(page)
	except PageNotAnInteger:
		propiedades = paginator.page(1)
	except EmptyPage:
		propiedades = paginator.page(paginator.num_pages)

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
	page = request.GET.get('page', 1)
	lista_publicaciones = Publicacion.objects.all()

	paginator = Paginator(lista_publicaciones, 10)

	try:
		publicaciones = paginator.page(page)
	except PageNotAnInteger:
		publicaciones = paginator.page(1)
	except EmptyPage:
		publicaciones = paginator.page(paginator.num_pages)

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