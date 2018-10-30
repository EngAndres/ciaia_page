from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Attender
from .models import Category


# Create your views here.
def index(request):
	return render(request, 'ciaia/index.html')

def agenda(request):
	return render(request, 'ciaia/agenda.html')

def comite(request):
	return render(request, 'ciaia/comite.html')

def conferencistas(request):
	return render(request, 'ciaia/conferencistas.html')

def entidades(request):
	return render(request, 'ciaia/entidades.html')

def registro(request):
	return render(request, 'ciaia/preregistro.html')

def venue(request):
	return render(request, 'ciaia/venue.html')
