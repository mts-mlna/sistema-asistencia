import datetime
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

logger = logging.getLogger(__name__)

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
           user = form.get_user()
           login(request, user)
           logger.info(f"Usuario {user.username} ha iniciado sesión.")
           return redirect('home')
        else:
            logger.warning("No se inició sesión:{form.errors.as_json()}")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required

def cerrar_sesion(request):
    logger.info(f"Usuario {request.user.username} ha cerrado sesión.")
    logout(request)
    return redirect('home')


def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            empleado = Empleado.objects.create(
                usuario=user,
                dni=form.cleaned_data['dni'],
                telefono=form.cleaned_data['telefono'],
                cargo=form.cleaned_data['cargo']
            )
            login(request, user)
            logger.info(f"👨‍🏫 Registro exitoso de empleado: {user.username} - Cargo: {empleado.cargo}")
            return redirect('home')
        else:
            logger.warning(f"❌ Error en registro de empleado: {form.errors.as_json()}")
    else:
        form = EmpleadoForm()
    return render(request, 'registrarse.html', {'form': form})

def registrar_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            administrador = Administrador.objects.create(
                usuario=user,
                dni=form.cleaned_data['dni'],
                telefono=form.cleaned_data['telefono']
            )
            login(request, user)
            logger.info(f"🛠️ Registro exitoso de administrador: {user.username}")
            return redirect('home')
        else:
            logger.warning(f"❌ Error en registro de administrador: {form.errors.as_json()}")
    else:
        form = AdministradorForm()
    return render(request, 'registrarse.html', {'form': form})
