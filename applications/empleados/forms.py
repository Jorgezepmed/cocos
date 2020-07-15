from django import forms

from .models import empleados

class empleadoForm(forms.ModelForm):
    
    class Meta:
        model = empleados
        fields = (
            'name',
            'last_name',
            'cel',
            'id',
            
            #'avatar',
            
        )
       
