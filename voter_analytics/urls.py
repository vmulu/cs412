# File: voter_analytics/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 10/31/2025
# Description: Maps the URL patterns to the corresponding views for the Voter application.
from django.urls import path
from . import views

urlpatterns = [
	path(r'', views.VoterListView.as_view(), name='voters'),
    path(r'voters_list', views.VoterListView.as_view(), name='voters_list'),
    path(r'voter/<int:pk>/', views.VoterDetailView.as_view(), name='voter'),
    path(r'graphs/', views.VoterGraphsView.as_view(), name='voter_graphs'),
]