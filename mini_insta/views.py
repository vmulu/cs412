# File: mini_insta/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: defines the view functions and/or class-based views for the Django application.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Profile

# Create your views here.

class ProfileListView(ListView):
    """
    Displays a list of all Profile objects in the application.
    """

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    """
    Displays a single profile
    """
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"