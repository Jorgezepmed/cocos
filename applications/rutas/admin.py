from django.contrib import admin
from .models import rutas


class RutasAdmin(admin.ModelAdmin):
    list_display = (
        'ruta',
        
    )


admin.site.register(rutas, RutasAdmin)
