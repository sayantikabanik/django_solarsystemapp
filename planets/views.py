from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def planet_name(request):
	return HttpResponse("Earth")
