# File: project/admin.py
# Author: Victoria Mulugeta (vmulu@bu.edu)
# Description: register my model with the Django admin.

from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Activity)
admin.site.register(PackingList)