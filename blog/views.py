from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Article, Comment
from .forms import CreateArticleForm, CreateCommentForm, UpdateArticleForm
from django.urls import reverse
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
class ShowAllView(ListView):

    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

    def dispatch(self, request, *args, **kwargs):
        '''Override the dispatch method to add debugging information.'''

        if request.user.is_authenticated:
            print(f'ShowAllView.dispatch(): request.user={request.user}')
        else:
            print(f'ShowAllView.dispatch(): not logged in.')

        return super().dispatch(request, *args, **kwargs)

class ArticleView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"


class RandomArticleView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"

    def get_object(self):
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article

class CreateArticleView(LoginRequiredMixin, CreateView):

    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'CreateArticleView: form.cleaned_data={form.cleaned_data}')

        # find the logged in user
        user = self.request.user
        print(f"CreateArticleView user={user} article.user={user}")

        # attach user to form instance (Article object):
        form.instance.user = user

        return super().form_valid(form)

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')

class CreateCommentView(CreateView):

    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    def get_success_url(self):
        # return a url of what to do after success
        pk = self.kwargs['pk']
        # reverse builds url
        return reverse('article', kwargs={'pk': pk})

    def form_valid(self, form):
        # attaching foreign key and attaching it to the instance
        print(form.cleaned_data)
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        form.instance.article = article

        return super().form_valid(form)

    def get_context_data(self):
        context = super().get_context_data()
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)

        context['article'] = article

        return context


class UpdateArticleView(UpdateView):
    '''A view to update an Article and save it to the database.'''

    model = Article
    form_class = UpdateArticleForm
    template_name = "blog/update_article_form.html"

    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'UpdateArticleView: form.cleaned_data={form.cleaned_data}')


        return super().form_valid(form)

class DeleteCommentView(DeleteView):
    '''A view to delete a comment and remove it from the database.'''

    template_name = "blog/delete_comment_form.html"
    model = Comment
    context_object_name = 'comment'

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # get the pk for this comment
        pk = self.kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)

        # find the article to which this Comment is related by FK
        article = comment.article

        # reverse to show the article page
        return reverse('article', kwargs={'pk':article.pk})

class RegistrationView(CreateView):
    '''
    show/process form for account registration
    '''

    template_name = 'blog/register.html'
    form_class = UserCreationForm
    model = User

    def get_success_url(self):
        '''The URL to redirect to after creating a new User.'''
        return reverse('login')

# REST API:

from rest_framework import generics
from .serializers import *

class ArticleListAPIView(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
