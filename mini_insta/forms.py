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

