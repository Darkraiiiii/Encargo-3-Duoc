from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Animal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class AnimalForm(forms.ModelForm):
    class Meta:
        model= Animal
        fields = ['numero', 'animal', 'categoria','precio','visualizaciones','descripcion', 'imagen']
        labels={
            'numero':'Numero',
            'animal':'Animal',
            'categoria':'Categoria',
            'precio':'Precio',
            'visualizaciones':'Visualizaciones',
            'descripcion':'Descripcion',
            'imagen':'Imagen'
        }
        widgets={
            'numero': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una id..',
                    'id':'numero'
                }
            ),
            'animal':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Animal..',
                    'id': 'animal'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Precio..',
                    'id': 'Precio'
                }
            ),
            'visualizaciones':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Visualizaciones..',
                    'id': 'visualizaciones'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese descripción..',
                    'id': 'descripcion'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            )
        }