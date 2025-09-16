# File: restaurant/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/16/2025
# Description: Used to forward requests to the appropriate view

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.main_page, name="main_page"),
    path(r'order_page', views.order_page, name="order_page"),
    path(r'confirmation_page', views.confirmation_page, name="confirmation_page"),
]