# File: mini_insta/models.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: Defines the data models for the Django application.

from django.db import models

# Create your models here.

class Profile(models.Model):
    """
    Represents a user's profile in the application.
    """

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    join_date = models.DateTimeField(auto_now=True)
    bio_text = models.TextField(blank=True)

    def __str__(self):
        return f'username: {self.username} name: {self.display_name}'