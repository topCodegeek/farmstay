from django.shortcuts import render, get_object_or_404
from .models import Location

def home(request):
     locations = Location.objects.all()[:5]
     context = {'locations':locations}
     return render (request, 'home.html', context)

def locations(request):
     locations = Location.objects.all()
     context = {'locations':locations}
     return render (request, 'locations.html', context)

def view_location(request, id):
     location = get_object_or_404(Location, pk=id)
     context = {'location':location}
     return render(request, 'view_location.html', context)