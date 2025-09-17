# File: restaurant/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/16/2025
# Description: Is called by url.py and respond to request generating the UI

from django.shortcuts import render
import random

# Create your views here.

# daily special items that are picked at random
daily_special = [
    'Crazy Cheeseburger Meal',
    'Lazy Lasagna',
    'Corn on the Cob'
]

# standard menu items
menu_item = [
    'Chicken Finger Meal',
    'Tomato Basil Soup',
    'Cheese Pizza'
]

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

    context = {
        'daily_special': random.choice(daily_special),
        'menu_item_one': menu_item[0],
        'menu_item_two': menu_item[1],
        'menu_item_three': menu_item[2]
    }

    return render(request, template_name, context)

def confirmation_page(request):
    """
    the view to process the submission of an order, and display a confirmation page.
    """
    template_name = 'restaurant/confirmation_page.html'

    # add work

    return render(request, template_name)