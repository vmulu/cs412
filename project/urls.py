# File: project/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: Receiving HTTP requests and provides the corresponding view function

from django.urls import path
from . views import *

urlpatterns = [
    path('', TripListView.as_view(), name="all_trips"),
    path('trip/<int:pk>/', TripView.as_view(), name="trip"),
    path('destination/<int:pk>/', DestinationView.as_view(), name="destination"),
    path('create_trip', CreateTripFormView.as_view(), name="create_trip"),
    path('trip/<int:pk>/create_destination', CreateDestinationFormView.as_view(), name="create_destination"),
    path('trip/<int:pk>/create_packing_list', CreatePackingListFormView.as_view(), name="create_packing_list"),
    path('destination/<int:pk>/create_activity', CreateActivityFormView.as_view(), name="create_activity"),
    path('trip/<int:pk>/packing_list/update', UpdatePackingListFormView.as_view(), name="update_packing_list"),
]