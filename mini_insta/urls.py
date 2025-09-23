# File: mini_insta/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: Receiving HTTP requests and provides the corresponding view function

from django.urls import path
from . views import ProfileDetailView, ProfileListView
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
]