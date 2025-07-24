from home.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class LocationSerializer(ModelSerializer):
     class Meta:
          model = Location
          fields = ['id', 'name', 'description', 'thumbnail']

class ResortSerializer(ModelSerializer):
     class Meta:
          model = Resort
          fields = ['id', 'name', 'description', 'thumbnail', 'rating', 'location']

