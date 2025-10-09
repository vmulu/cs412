# from second example videos
from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            'author',
            'title',
            'text',
            #'image_url',
            'image_file'
        ]

class UpdateArticleForm(forms.ModelForm):
    '''A form to update a quote to the database.'''

    class Meta:
        '''associate this form with the Article model.'''
        model = Article
        fields = ['title', 'text', ]  # which fields from model should we use

class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            # 'article',
            'author',
            'text'
        ]
