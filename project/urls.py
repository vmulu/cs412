# File: project/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: Receiving HTTP requests and provides the corresponding view function

from django.urls import path
from . views import *

urlpatterns = [
    path('', TripListView.as_view(), name="all_trips"),
    path('trip/<int:pk>/', TripView.as_view(), name="trip"),
    path('destination/<int:pk>/', DestinationView.as_view(), name="destination"),
]