from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as Usuario

from .models import Tipo, Propiedad, Imagen, Detalle, Categoria, Publicacion, InformacionExtra

# ajustes en alta de usuarios
class InformacionExtraInline(admin.StackedInline):
	model = InformacionExtra
	can_delete = False
	verbose_name_plural = 'informacion'

class UsuarioAdmin(BaseUserAdmin):
    inlines = (InformacionExtraInline,)
# ajustes en alta de usuarios

# propiedades
class TipoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class DetalleAdmin(admin.StackedInline):
	model = Detalle
	extra = 1
	max_num = 0
	can_delete = False

class ImagenAdmin(admin.TabularInline):
	model = Imagen

class PropiedadAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'precio', 'opcion', 'ubicacion', 'tipo')
	search_fields = ('titulo', 'ubicacion')
	list_filter = ['destacado', 'tipo__nombre']
	list_per_page = 10
	inlines = [
		DetalleAdmin,
		ImagenAdmin
	]

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(asesor=request.user)
# propiedades

# blog
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class PublicacionAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'categoria', 'autor', 'fecha')
	search_fields = ('titulo',)
	list_filter = ['autor', 'categoria__nombre', 'fecha']
# blog

admin.site.unregister(Usuario)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
