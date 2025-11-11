from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .validators import validate_cpf, validate_phone, format_cpf, format_phone

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='Nome')
    last_name = forms.CharField(required=True, label='Sobrenome')
    phone_number = forms.CharField(required=True, label='Telefone')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar as mensagens de ajuda
        self.fields['username'].help_text = 'Necessário. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'
        self.fields['password1'].help_text = 'Sua senha deve conter pelo menos 8 caracteres.'
        self.fields['password2'].help_text = 'Digite a mesma senha novamente para verificação.'
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder': '(00) 00000-0000'})

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            is_valid, message = validate_phone(phone)
            if not is_valid:
                raise forms.ValidationError(f'Telefone inválido: {message}')
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Criar perfil automaticamente com o número de telefone
            phone = self.cleaned_data['phone_number']
            Profile.objects.create(
                user=user,
                phone_number=format_phone(phone)
            )
        return user

class LoginRegisterForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'cpf', 'phone_number', 'address']
        labels = {
            'profile_pic': 'Foto de perfil',
            'cpf': 'CPF',
            'phone_number': 'Telefone',
            'address': 'Endereço'
        }
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'Seu endereço completo'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '(00) 00000-0000 ou 00000000000', 
                'class': 'form-control'
            }),
            'cpf': forms.TextInput(attrs={
                'placeholder': '000.000.000-00 ou 00000000000', 
                'class': 'form-control',
                'maxlength': '14'
            }),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:  # Só valida se foi preenchido
            is_valid, message = validate_cpf(cpf)
            if not is_valid:
                raise forms.ValidationError(f'CPF inválido: {message}')
            # Verifica unicidade (exceto o próprio usuário)
            existing = Profile.objects.filter(cpf=cpf).exclude(user=self.instance.user)
            if existing.exists():
                raise forms.ValidationError('Este CPF já está cadastrado')
        return cpf
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:  # Só valida se foi preenchido
            is_valid, message = validate_phone(phone)
            if not is_valid:
                raise forms.ValidationError(f'Telefone inválido: {message}')
        return phone
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        # Formatar CPF e telefone antes de salvar
        if profile.cpf:
            profile.cpf = format_cpf(profile.cpf)
        if profile.phone_number:
            profile.phone_number = format_phone(profile.phone_number)
        if commit:
            profile.save()
        return profile
