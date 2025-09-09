# File: quotes/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/9/2025
# Description: Is called by url.py and respond to request generating the UI

from django.shortcuts import render
import random
import time

# Create your views here.

# list of quotes 
quotes = [
    "Don't be afraid of failure. This is the way to succeed.",
    "You have to be able to accept failure to get better.",
    "You have to earn your leadership every day.",
]

# list of image URLs 
image_URLs = [
    "https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_xl_2x/f_auto/primary/c5r52rbifxn2srhp9no0",
    "https://a57.foxsports.com/statics.foxsports.com/www.foxsports.com/content/uploads/2025/07/1294/728/lebron2.jpg?ve=1&tl=1",
    "https://observer.case.edu/wp-content/uploads/2021/02/sports2-900x600.jpg",

]

def quote_page(request):
    """
    The view for the main page that will select one quote and one image at random 
    """

    template_name = 'quotes/quote.html'
    context = {
       "rand_quote" : random.choice(quotes),
       "rand_img" : random.choice(image_URLs),
       "time": time.ctime(),
    }

    return render(request, template_name, context)

def show_all(request):
    """
    Adds the entire list of quotes and images to the context data for the view
    """

    template_name = 'quotes/show_all.html'
    context = {
        "q1" : quotes[0],
        "q2" : quotes[1],
        "q3" : quotes[2],
        "img1" : image_URLs[0],
        "img2" : image_URLs[1],
        "img3" : image_URLs[2],
        "time": time.ctime(),
    }

    return render(request, template_name, context)

def about_page(request):
    """
    Displays information about the famous person whose quotes are shown in this
    application (Lebron James).
    """

    template_name = 'quotes/about.html'
    context = {
        "time": time.ctime(),
    }
    
    return render(request, template_name, context)

