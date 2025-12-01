# File: project/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: Defines the view functions and/or class-based views for the Django application.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import *

# Create your views here.

class TripListView(ListView):
    """
    View to see all trips
    """

    model = Trip
    template_name = 'project/trips.html'
    context_object_name = 'trips'

class TripView(DetailView):
    """
    View to see a trips information
    """

    model = Trip
    template_name = 'project/trip.html'
    context_object_name = 'trip'

class DestinationView(DetailView):
    """
    View to see destination
    """

    model = Destination
    template_name = 'project/destination.html'
    context_object_name = 'destination'

