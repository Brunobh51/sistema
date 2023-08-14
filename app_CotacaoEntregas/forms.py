from django import forms
from .models import Cliente

"""
    class FormularioCadastro(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
"""


class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'n_pedido', 'telefone']
