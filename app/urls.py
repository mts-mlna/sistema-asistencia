from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    # path('registrar/alumno/', registrar_alumno, name='registrar_alumno'),
    path('registrar/empleado/', registrar_empleado, name='registrar_empleado'),
    path('registrar/administrador/', registrar_administrador, name='registrar_administrador'),
]
