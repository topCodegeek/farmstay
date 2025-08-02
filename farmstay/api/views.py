from django.contrib.auth.models import User
from home.models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import BasePermission

APP_NAME = "api"

# IsStaff permission class
class IsStaff(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

# Views
class UserListView(generics.ListAPIView):
     serializer_class = UserSerializer
     permission_classes = [IsStaff]
     queryset = User.objects.all()

class UserRetrieve(generics.RetrieveAPIView):
     serializer_class = UserSerializer
     permission_classes = [IsStaff]
     queryset = User.objects.all()

     def get_object(self):
          return super().get_object()

class LocationsListView(generics.ListCreateAPIView):
     serializer_class = LocationSerializer
     permission_classes = [IsStaff]
     queryset = Location.objects.all()

class ResortsListView(generics.ListCreateAPIView):
     serializer_class = ResortSerializer
     permission_classes = [IsStaff]
     queryset = Resort.objects.all()

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = LocationSerializer
     permission_classes = [IsStaff]
     queryset = Location.objects.all()
     
     def get_queryset(self):
          return super().get_queryset()
     
class ResortRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = ResortSerializer
     permission_classes = [IsStaff]
     queryset = Resort.objects.all()

     def get_queryset(self):
          return super().get_queryset()