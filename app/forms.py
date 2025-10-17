from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Asistencia, Alumno, Empleado, Administrador

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['nombre', 'apellido', 'materia', 'presente']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'materia': forms.TextInput(attrs={'class': 'form-control'}),
            'presente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
# class AlumnoForm(UserCreationForm):
#     class Meta:
#         model = Alumno
#         fields = ['username', 'password1', 'password2', 'dni', 'telefono']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'dni': forms.TextInput(attrs={'class': 'form-control'}),
#             'telefono': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class EmpleadoForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cargo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class AdministradorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

