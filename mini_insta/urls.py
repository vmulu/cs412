# File: mini_insta/urls.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: Receiving HTTP requests and provides the corresponding view function

from django.urls import path
from . views import *
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('profile/<int:pk>/create_post/', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='following'),
    path('profile/<int:pk>/feed', PostFeedListView.as_view(), name='feed'),
    path('profile/<int:pk>/search', SearchView.as_view(), name='search')
]