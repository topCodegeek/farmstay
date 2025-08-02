from django.contrib.auth.models import User
from home.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
     class Meta:
          model = User
          fields = ['id', 'username', 'first_name', 'last_name', 'email']

class LocationSerializer(ModelSerializer):
     class Meta:
          model = Location
          fields = ['id', 'name', 'description', 'thumbnail']

class ResortSerializer(ModelSerializer):
     class Meta:
          model = Resort
          fields = ['id', 'name', 'description', 'thumbnail', 'rating', 'location']

