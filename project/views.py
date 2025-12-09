# File: project/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: Defines the view functions and/or class-based views for the Django application.

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . models import *
from . forms import *

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

class CreateTripFormView(CreateView):
    """
    View class for creating a new Trip object
    """

    form_class = CreateTripForm
    template_name = "project/create_trip_form.html"

    def get_success_url(self):
        """
        Redirects to the newly created Trip's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('trip', kwargs={'pk': pk})

class CreateDestinationFormView(CreateView):
    """
    View class for creating a new Destination object
    """

    form_class = CreateDestinationForm
    template_name = "project/create_destination_form.html"

    def get_success_url(self):
        """
        Redirects to the newly created Destination's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('destination', kwargs={'pk': pk})

    def get_context_data(self):
        """
        Adds the trip object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        trip = Trip.objects.get(pk=pk)

        context['trip'] = trip

        return context

    def form_valid(self, form):
        """
        Attaching trip before saving to db
        """
        destination = form.save(commit=False)
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        destination.trip = trip
        destination.save()
        return super().form_valid(form)

class CreatePackingListFormView(CreateView):
    """
    View class for creating a packinglist
    """

    form_class = CreatePackingListForm
    template_name = "project/create_packing_list.html"

    def get_success_url(self):
        """
        Redirects to the newly created Trip's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('trip', kwargs={'pk': pk})

    def get_context_data(self):
        """
        Adds the trip object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        trip = Trip.objects.get(pk=pk)

        context['trip'] = trip

        return context

    def form_valid(self, form):
        """
        Attaching trip before saving to db
        """
        destination = form.save(commit=False)
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        destination.trip = trip
        destination.save()
        return super().form_valid(form)

class CreateActivityFormView(CreateView):
    """
    Activity form view
    """

    form_class = CreateActivitiesForm
    template_name = "project/create_activity_form.html"

    def get_success_url(self):
        """
        Redirects to the newly created Destination's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('destination', kwargs={'pk': pk})

    def get_context_data(self):
        """
        Adds the trip object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        destination = Destination.objects.get(pk=pk)

        context['destination'] = destination

        return context

    def form_valid(self, form):
        """
        attaching destination pk to activity
        """
        destination = get_object_or_404(Destination, pk=self.kwargs["pk"])
        activity = form.save(commit=False)
        activity.destination = destination
        activity.save()
        self.object = activity
        return redirect("destination", pk=destination.pk)

class UpdatePackingListFormView(UpdateView):
    """
    View for updating packing list
    """

    model = PackingList
    template_name = 'project/update_packing_list.html'
    form_class = UpdatePackingListForm

    def get_context_data(self):
        """
        Adds the trip object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        trip = Trip.objects.get(pk=pk)

        context['trip'] = trip

        return context

    def get_success_url(self):
        """
        Redirects to the newly created Trip's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('trip', kwargs={'pk': pk})
