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

    def get_all_posts(self):
        """
        finds and returns all Posts for a given Profile
        """
        posts = Post.objects.filter(profile=self)
        return posts

class Post(models.Model):
    """
    Represents a user's post on their profile
    """

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.caption}'

    def get_all_photos(self):
        """
        finds and returns all Photos for a given Post.
        """
        photos = Photo.objects.filter(post=self).order_by('timestamp')
        return photos

class Photo(models.Model):
    """
    Represents the data attributes of an image associated with a Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'comment for {self.post} at {self.timestamp}'