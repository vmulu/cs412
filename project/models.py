# project/models.py
# Victoria Mulugeta (vmulu@bu.edu)
# Defining data structure of database

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Trip(models.Model):
    """
    Stores information about a single trip
    """

    # need to change this back when i add users
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_all_destinations(self):
        """
        finds and returns all destinations for a given trip
        """
        destinations = Destination.objects.filter(trip=self)
        return destinations

    def get_packing_list(self):
        """
        finds and returns packing list for a given trip
        """
        packing_list = PackingList.objects.get(trip=self)
        return packing_list

    def get_absolute_url(self):
        """
        returns the URL corresponding to the trip
        """
        return reverse('trip', kwargs={'pk': self.pk})

class Destination(models.Model):
    """
    Stores information about a travel destination
    """

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='destinations')
    name = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    arrival_date = models.DateField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} Destination for {self.trip.name} Trip"

    def get_all_activities(self):
        """
        finds and returns packing activities for a given trip
        """
        activities = Activity.objects.filter(destination=self)
        return activities

class Activity(models.Model):
    """
    Stores an activity planned for a trip
    """

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='activities')
    name = models.TextField(blank=True)
    time = models.DateTimeField(null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PackingList(models.Model):
    """
    Stores packing list for a trip
    """

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='packing_items')
    name = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=1)
    is_packed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
