from django.contrib import admin
from .models import empleados



class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'cel',
    )

admin.site.register(empleados, EmpleadosAdmin)