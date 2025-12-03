# File: project/forms.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: Defines the form for creating a new Trip and Destination

from django import forms
from .models import *

class CreateTripForm(forms.ModelForm):
    """
    Form for creating a new Trip
    """

    class Meta:
        model = Trip
        fields = [
            'name',
            'start_date',
            'end_date',
            'notes',
            'is_completed',
        ]

class CreateDestinationForm(forms.ModelForm):
    """
    Form for creating a new Destination
    """

    class Meta:
        model = Destination
        fields = [
            'name',
            'order',
            'arrival_date',
            'departure_date',
            'notes',
        ]
