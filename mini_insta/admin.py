# File: mini_insta/admin.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: register my model with the Django admin.

from django.contrib import admin

# Register your models here.

from . models import Profile
admin.site.register(Profile)
