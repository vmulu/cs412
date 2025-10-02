# File: mini_insta/forms.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 10/2/2025
# Description: add description

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''
    add doc string
    '''

    class Meta:
        model = Post
        fields = [
            'caption',
        ]

