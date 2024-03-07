from django import forms
from django.contrib.auth.models import User
from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['created_by'].initial = 1

    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'nome': 'Nome da fotografia',
            'descricao': 'Descrição',
            'created_at': 'Data de registro',
            'created_by': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'created_by': forms.Select(
                attrs={'class': 'form-control'},
            ),
        }
