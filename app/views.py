from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import logout
from django.db.models import Q
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')