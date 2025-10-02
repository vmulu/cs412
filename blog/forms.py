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
            'image_url'
        ]

class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            # 'article',
            'author',
            'text'
        ]