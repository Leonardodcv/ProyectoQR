from django.contrib import admin
from .models import Os,Tipo,Equipo, Fabricante
# Register your models here.
#admin.site.register(Os)
#admin.site.register(Tipo)
#admin.site.register(Equipo)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display=["ns","fabricante","tipo","discoDuro","ram"]


@admin.register(Os)
class OsAdmin(admin.ModelAdmin):
    list_display=["nombre"]

@admin.register(Tipo)
class TipoInstanceAdmin(admin.ModelAdmin):
    list_display=["nombre"]

@admin.register(Fabricante)
class FabricanteInstanceAdmin(admin.ModelAdmin):
    list_display=["nombre"]