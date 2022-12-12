from django import forms
from ejemplo.models import Familiar, Juegos

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busca algo...'}))


class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']

class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = ['nombre', 'tipo']