# File: restaurant/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/16/2025
# Description: Is called by url.py and respond to request generating the UI

from django.shortcuts import render
import random

# Create your views here.

# daily special items that are picked at random
daily_special = [
    'Crazy Cheeseburger Meal $12.00',
    'Lazy Lasagna $23.10',
    'Corn on the Cob $2.30'
]

# standard menu items
menu_item = {
    'Chicken Finger Meal' : 5.20,
    'Tomato Basil Soup' : 6.40,
    'Cheese Pizza' : 10.20,
    'Crazy Cheeseburger Meal' : 12.00,
    'Lazy Lasagna' : 23.10,
    'Corn on the Cob' : 2.30,
    'Extra Cheese' : 1.00
}


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

    menu_items = list(menu_item.keys())

    context = {
        'daily_special': random.choice(daily_special),
        'menu_item_one': menu_items[0],
        'menu_item_two': menu_items[1],
        'menu_item_three': menu_items[2],
        'extra': menu_items[6]
    }

    return render(request, template_name, context)

def confirmation_page(request):
    """
    the view to process the submission of an order, and display a confirmation page.
    """
    template_name = 'restaurant/confirmation_page.html'
    print(request.POST)

    if request.POST:
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        total_food = request.POST.getlist('food')

        context = {
            'name': name,
            'number': number,
            'email': email,
            'food': total_food,
        }


    return render(request, template_name, context)