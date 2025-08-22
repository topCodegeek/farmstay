from django.contrib.auth.models import User
from home.models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import *
from rest_framework.exceptions import ValidationError

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
     
class CouponsListView(generics.ListCreateAPIView):
     serializer_class = CouponSerializer
     permission_classes = [IsAuthenticated]

     def get_queryset(self):
          if self.request.user.username!='ishaantopkar':
               raise ValidationError({'El bozo (400)': 'Got you nerd 😜', 'message':"Don't worry ur data isn't saved 🙂"})
          else:
               return Coupon.objects.all()