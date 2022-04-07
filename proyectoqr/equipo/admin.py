from django.contrib import admin
from .models import Os,Tipo,Equipo
# Register your models here.
#admin.site.register(Os)
#admin.site.register(Tipo)
#admin.site.register(Equipo)

class EquipoAdmin(admin.ModelEquipo):
    pass


@admin.register(Os)
class OsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tipo)
class TipoInstanceAdmin(admin.ModelAdmin):
    pass