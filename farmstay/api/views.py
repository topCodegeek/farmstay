from django.shortcuts import render
from home.models import *
from rest_framework import generics, permissions
from .serializers import *

APP_NAME = "api"

class LocationsListView(generics.ListCreateAPIView):
     serializer_class = LocationSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     queryset = Location.objects.all()

class ResortsListView(generics.ListCreateAPIView):
     serializer_class = ResortSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     queryset = Resort.objects.all()

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = LocationSerializer
     permission_classes = [permissions.IsAuthenticated]
     queryset = Location.objects.all()
     
     def get_queryset(self):
          return super().get_queryset()
     
class ResortRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = ResortSerializer
     permission_classes = [permissions.IsAuthenticated]
     queryset = Resort.objects.all()

     def get_queryset(self):
          return super().get_queryset()