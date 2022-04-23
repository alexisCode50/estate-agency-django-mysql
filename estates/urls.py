from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('properties/', views.properties, name='properties'),
	path('properties/<int:id>/', views.single_propety, name='single_propety'),
	path('properties/contact/adviser', views.contact_adviser, name='contact_adviser'),
	path('blog/', views.blog, name='blog'),
	path('blog/<int:id>/', views.single_blog, name='single_blog'),
	path('contact/', views.contact, name='contact'),
]