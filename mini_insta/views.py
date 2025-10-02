# File: mini_insta/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: defines the view functions and/or class-based views for the Django application.

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from . models import Profile, Post, Photo
from . forms import CreatePostForm

# Create your views here.

class ProfileListView(ListView):
    """
    Displays a list of all Profile objects in the application.
    """

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    """
    Displays a single profile
    """
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

class PostDetailView(DetailView):
    """
    Displays a single post
    """
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    """
    View for the creating a post page
    """

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        """
        Adds the profile object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile

        return context

    def form_valid(self, form):
        """
        Handles the form submission and processes the data.
        """
        # attaching foreign key and attaching it to the instance
        print(form.cleaned_data)
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        post = form.save()

        # attaching photo to post
        image_url = self.request.POST.get('image_url')
        if image_url:
            photo = Photo(post=post, image_url=image_url)
            photo.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirects to the newly created Post's detail page.
        """
        # return a url of what to do after success
        pk = self.object.pk
        # reverse builds url
        return reverse('post', kwargs={'pk': pk})