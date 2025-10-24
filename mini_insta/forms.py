# File: mini_insta/forms.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 10/2/2025
# Description: Defines the form for creating a new Post, including the caption field.

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''
    Form for creating a new Post associated with a Profile.
    '''

    class Meta:
        model = Post
        fields = [
            'caption',
        ]

class UpdateProfileForm(forms.ModelForm):
    """
    Form for updating a profile
    """

    class Meta:
        model = Profile
        fields = [
            'display_name',
            'profile_image_url',
            'bio_text'
        ]

class UpdatePostForm(forms.ModelForm):
    """
    Form for updating a post
    """

    class Meta:
        model = Post
        fields = [
            'caption',
        ]

class CreateProfileForm (forms.ModelForm):
    """
    form for creating a profile
    """

    class Meta:
        model = Profile
        fields = [
            'username',
            'display_name',
            'bio_text',
            'profile_image_url'
        ]