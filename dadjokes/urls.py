# urls.py

from django.urls import path
from . views import *


urlpatterns = [
    path('', RandomJokeView.as_view(), name='home'),
    path('random', RandomJokeView.as_view(), name='random_jokes'),
    path('jokes', AllJokesView.as_view(), name='all_jokes'),
    path('joke/<int:pk>', JokeView.as_view(), name='joke'),
    path('pictures', AllPictureView.as_view(), name='all_pictures'),
    path('picture/<int:pk>', PictureView.as_view(), name='picture'),

    # API VIEWS:
    path('api/', RandomJokeAPIView.as_view(), name='joke_api' ),
    path('api/random', RandomJokeAPIView.as_view(), name='random_joke_api'),
    path('api/jokes', JokesListAPIView.as_view(), name='all_jokes_api'),
    path('api/joke/<int:pk>', OneJokeAPIView.as_view(), name='one_joke_api'),
    path('api/pictures', PicturesListAPIView.as_view(), name='all_pictures_api'),
    path('api/picture/<int:pk>', OnePictureAPIView.as_view(), name='one_picture_api'),
    path('api/random_picture', RandomPictureAPIView.as_view(), name='random_picture_api'),
]