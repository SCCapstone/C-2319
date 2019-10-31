from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def home(request):
	return render(request = request, 
				  template_name='home/home.html', 
				  context = {'title': 'Home Page'})

def about(request):
	return render(request = request, 
				  template_name='home/about.html', 
				  context = {'about': About.objects.all})
	

