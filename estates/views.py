from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.models import User as Usuario

from .models import Propiedad, Publicacion, Tipo

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
	busqueda = request.GET.get('busqueda')
	tipo = request.GET.get('tipo') or 1
	cuartos = request.GET.get('cuartos') or 1
	baños = request.GET.get('baños') or 1

	lista_propiedades = []
	tipos = Tipo.objects.all()

	if busqueda is not None and busqueda != '':
		lista_propiedades = Propiedad.objects.filter(
			titulo__icontains=busqueda,
			tipo__gte=tipo,
			detalles__cuartos__gte=cuartos,
			detalles__baños__gte=baños
		)
	else:
		lista_propiedades = Propiedad.objects.filter(
			tipo__gte=tipo,
			detalles__cuartos__gte=cuartos, 
			detalles__baños__gte=baños
		)

	paginator = Paginator(lista_propiedades, 10)

	try:
		propiedades = paginator.page(page)
	except PageNotAnInteger:
		propiedades = paginator.page(1)
	except EmptyPage:
		propiedades = paginator.page(paginator.num_pages)

	context = {
		'tipos': tipos,
		'propiedades': propiedades,
	}

	return render(request, 'estates/properties.html', context)

def single_propety(request, id):
	propiedad = get_object_or_404(Propiedad, pk=id)

	context = {
		'propiedad': propiedad
	}

	return render(request, 'estates/single-property.html', context)

def contact_adviser(request):
	propiedad_id = request.POST['propiedad_id']
	asesor_id = request.POST['asesor_id']
	nombre = request.POST['nombre']
	email = request.POST['email']
	comentarios = request.POST['comentarios']
	mensaje = {}

	asesor = get_object_or_404(Usuario, pk=asesor_id)
	propiedad = get_object_or_404(Propiedad, pk=propiedad_id)

	if asesor and propiedad:

		try:
			mail = create_mail(
				asesor.email,
				'Nuevo mensaje',
				'adviser-mail.html',
				{
					'propiedad_id': propiedad.id,
					'propiedad_titulo': propiedad.titulo,
					'nombre': nombre,
					'email': email,
					'comentarios': comentarios,
				}
			)

			mail.send(fail_silently=False)

			mensaje = {
				'ok': True,
				'mensaje': 'El mensaje se envio con exito' 
			}

		except:
			mensaje = {
				'ok': False,
				'mensaje': 'Ocurrio un error al enviar el mensaje, intentalo de nuevo' 
			}
		
	return JsonResponse(mensaje)

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

def create_mail(user_mail, subject, template_name, context):
	template = render_to_string('estates/' + template_name, context)

	message = EmailMultiAlternatives(
    	subject=subject,
    	body='',
    	from_email=settings.EMAIL_HOST_USER,
    	to=[
            user_mail
		],
		cc=[]
	)

	message.attach_alternative(template, 'text/html')

	return message