from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Location

def login_with_google(request):
    url = reverse("google_login")
    return redirect(url)

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