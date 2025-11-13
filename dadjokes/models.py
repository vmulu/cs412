from django.db import models

# Create your models here.

class Joke(models.Model):
    """
    Joke model
    """

    text = models.TextField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} wrote this joke"

class Picture(models.Model):
    """
    Picture model
    """

    image_url = models.URLField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} put this image"