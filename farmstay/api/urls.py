from django.urls import path, include
from .views import *

APP_NAME = 'api'

urlpatterns = [
     path('', include('rest_framework.urls')),
     path('locations', LocationsListView.as_view()),
     path('locations/<int:pk>', LocationRetrieveUpdateDestroyView.as_view()),
     path('resorts', ResortsListView.as_view()),
     path('resorts/<int:pk>', ResortRetrieveUpdateDestroyView.as_view()),
]