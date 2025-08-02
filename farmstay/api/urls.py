from django.urls import path, include
from .views import *

APP_NAME = 'api'

urlpatterns = [
     # auth
     path('', include('rest_framework.urls')),

     # endpoints
     path('users', UserListView.as_view()),
     path('user/<int:pk>', UserRetrieve.as_view()),
     path('locations', LocationsListView.as_view()),
     path('locations/<int:pk>', LocationRetrieveUpdateDestroyView.as_view()),
     path('resorts', ResortsListView.as_view()),
     path('resorts/<int:pk>', ResortRetrieveUpdateDestroyView.as_view()),
]