from django import forms
from .models import Cliente, Endereco

"""
    class FormularioCadastro(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
"""


class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class FormularioEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
        
