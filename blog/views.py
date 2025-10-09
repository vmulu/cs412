from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Article, Comment
from .forms import CreateArticleForm, CreateCommentForm, UpdateArticleForm
from django.urls import reverse
import random

# Create your views here.
class ShowAllView(ListView):

    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

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

class CreateArticleView(CreateView):

    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

    def form_valid(self, form):
        print(f'CreateArticleView: form.cleaned_data={form.cleaned_data}')
        # delegate work to the superclass version of this method
        return super().form_valid(form)

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