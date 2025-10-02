from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Article
from .forms import CreateArticleForm, CreateCommentForm
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

