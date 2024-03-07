from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: António Marques',
            }
        ),
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )


class CadastroForms(forms.Form):
    nome_usuario = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: António Marques'
            }
        )
    )

    email_usuario = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: enderecomail@maildominio.com'
            }
        )
    )

    senha_usuario = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )

    senha_usuario_confirma = forms.CharField(
        label='Confirme a sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite novamente a sua senha',
            }
        )
    )

    def clean_nome_usuario(self):
        nome = self.cleaned_data.get('nome_usuario')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome do usuário não pode conter espaços')
            else:
                return nome

    def clean_senha_usuario_confirma(self):
        senha_1 = self.cleaned_data.get('senha_usuario')
        senha_2 = self.cleaned_data.get('senha_usuario_confirma')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return senha_2
