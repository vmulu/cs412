# File: restaurant/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/16/2025
# Description: Is called by url.py and respond to request generating the UI

from django.shortcuts import render
import random

# Create your views here.

def main_page(request):
    """
    view for the main page
    """

    template_name = 'restaurant/main_page.html'

    return render(request, template_name)

def order_page(request):
    '''
    view for the order page that displays a daily special
    '''

    template_name = 'restaurant/order_page.html'

    # add work

    return render(request, template_name)

def confirmation_page(request):
    """
    the view to process the submission of an order, and display a confirmation page.
    """
    template_name = 'restaurant/confirmation_page.html'

    # add work

    return render(request, template_name)