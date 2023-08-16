from django import forms
from .models import Cliente, Endereco

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class FormularioEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
        
