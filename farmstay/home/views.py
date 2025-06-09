from django.shortcuts import render
from .models import Location

def home(request):
     locations = Location.objects.all()
     context = {'locations':locations}
     return render (request, 'home.html', context)
