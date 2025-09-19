# File: restaurant/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/16/2025
# Description: Is called by url.py and respond to request generating the UI

from datetime import timedelta
from django.shortcuts import render
import random
from django.utils import timezone

# Create your views here.

# daily special items that are picked at random
daily_special = [
    'Crazy Cheeseburger Meal $12',
    'Lazy Lasagna $23',
    'Corn on the Cob $2'
]

# standard menu items
menu_item = {
    'Chicken Finger Meal' : 5,
    'Tomato Basil Soup' : 6,
    'Cheese Pizza' : 10,
    'Crazy Cheeseburger Meal $12' : 12,
    'Lazy Lasagna $23' : 23,
    'Corn on the Cob $2' : 2,
    'Extra Cheese' : 1
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
        random_min = random.randint(30, 60)
        current_time = timezone.now()
        ready_time = current_time + timedelta(minutes=random_min)

        special_instructions = request.POST['special_instructions']

        # fix for daily special
        total_price = 0
        for item in total_food:
            total_price += menu_item[item]

        context = {
            'name': name,
            'number': number,
            'email': email,
            'food': total_food,
            'ready_time': ready_time,
            'total_price': total_price,
            'special_instructions' : special_instructions
        }


    return render(request, template_name, context)