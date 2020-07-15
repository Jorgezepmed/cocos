from django import forms

class NewRutaForm(forms.Form):
    ruta = forms.CharField(max_length=50)