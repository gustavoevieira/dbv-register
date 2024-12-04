from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    aceitou_regimento = forms.BooleanField(label="Eu aceito o regimento interno do clube", required=True)
    
    class Meta:
        model = Registro
        fields = ['nome', 'email', 'telefone', 'aceitou_regimento']
