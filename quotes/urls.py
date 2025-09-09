# File: quotes/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/9/2025
# Description: Used to forward requests to the appropriate view

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    #path(r'', views.home_page, name="home_page"),
    path(r'', views.about_page, name="about_page"),
    path(r'show_all', views.show_all, name="show_all"),
    path(r'quote', views.quote_page, name="quote_page"),
]