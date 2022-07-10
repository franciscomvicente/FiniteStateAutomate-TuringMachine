from django import forms
from django.forms import ModelForm
from .models import AFD
from .models import TM


class AFDForm(ModelForm):
    class Meta:
        model = AFD
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do afd...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alfabeto do afd...'}),
            'estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estados do afd...'}),
            'estadoinicial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estado inicial do afd...'}),
            'estadosdeaceitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estados de aceitação do afd...'}),
            'tabeladetransicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'transições do afd...'}),
        }

class SequenciaForm(forms.Form):
    sequencia = forms.CharField()

class TMForm(ModelForm):
    class Meta:
        model = TM
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tm...'}),
            'estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estados da tm...'}),
            'estadoinicial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estado inicial da tm...'}),
            'estadodeaceitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estado de aceitacao da tm...'}),
            'tabeladetransicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'transicoes da tm...'}),
        }

class SequenciaTMForms(forms.Form):
    sequenciaTM = forms.CharField()