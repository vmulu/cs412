# File: mini_insta/admin.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: register my model with the Django admin.

from django.contrib import admin

# Register your models here.

from . models import Profile, Post, Photo
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)