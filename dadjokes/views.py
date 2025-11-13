from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *
import random

# Create your views here.

class RandomJokeView(DetailView):
    """
    view for main page
    """

    model = Joke
    template_name = 'dadjokes/jokes.html'
    context_object_name = 'jokes'

    def get_context_data(self, **kwargs):
        """
        adding random picture context
        """

        context = super().get_context_data(**kwargs)
        context['picture'] = self.get_object().get('picture')
        context['joke'] = self.get_object().get('joke')

        return context

    def get_object(self, queryset = None):
        """
        getting joke and picture
        """

        all_jokes = Joke.objects.all()
        all_pics = Picture.objects.all()

        context = {
            'joke': random.choice(all_jokes),
            'picture': random.choice(all_pics)
        }

        return context

class AllJokesView(ListView):
    """
    shows all jokes no images
    """

    model = Joke
    template_name = 'dadjokes/all_jokes.html'
    context_object_name = 'jokes'

    def get_context_data(self, **kwargs):
        """
        adding all jokes to context
        """
        context = super().get_context_data(**kwargs)

        context["all_jokes"] = Joke.objects.all()

        return context

class JokeView(DetailView):
    """
    showing a singular joke
    """

    model = Joke
    template_name = 'dadjokes/one_joke.html'
    context_object_name = 'joke'

class AllPictureView(ListView):
    """
    shows all pictures
    """

    model = Picture
    template_name = 'dadjokes/all_pictures.html'
    context_object_name = 'pictures'

    def get_context_data(self, **kwargs):
        """
        adding all pictures to context
        """
        context = super().get_context_data(**kwargs)

        context["all_pics"] = Picture.objects.all()

        return context

class PictureView(ListView):
    """
    shows one picture
    """

    model = Picture
    template_name = 'dadjokes/one_picture.html'
    context_object_name = 'picture'

    def get_object(self, queryset=None):
        """
        getting specific picture by pk
        """
        pk = self.kwargs.get('pk')
        picture = Picture.objects.get(pk=pk)
        return picture

# API Views
from rest_framework import generics
from .serializer import *

class RandomJokeAPIView(generics.RetrieveAPIView):
    """
    view for one random joke api
    """
    serializer_class = JokeSerializer

    def get_object(self):
        """
        getting random joke object
        """
        all_jokes = Joke.objects.all()
        return random.choice(all_jokes)

class JokesListAPIView(generics.ListCreateAPIView):
    """
    json rep of all jokes
    """

    serializer_class = JokeSerializer
    queryset = Joke.objects.all()

class OneJokeAPIView(generics.RetrieveAPIView):
    """
    view for one random joke api
    """
    serializer_class = JokeSerializer

    def get_object(self):
        """
        getting joke by pk
        """
        pk = self.kwargs.get('pk')
        joke = Joke.objects.get(pk=pk)
        return joke

class PicturesListAPIView(generics.ListAPIView):
    """
    json of all picture objects
    """

    serializer_class = PictureSerializer
    queryset = Picture.objects.all()

class OnePictureAPIView(generics.RetrieveAPIView):
    """
    one picture object json
    """

    serializer_class = PictureSerializer

    def get_object(self):
        """
        getting pic by pk
        """
        pk = self.kwargs.get('pk')
        pic = Picture.objects.get(pk=pk)
        return pic

class RandomPictureAPIView(generics.RetrieveAPIView):
    """
    retrieves random picture object
    """

    serializer_class = PictureSerializer

    def get_object(self):
        """
        getting random picture object
        """
        all_pics = Picture.objects.all()
        return random.choice(all_pics)