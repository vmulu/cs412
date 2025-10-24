# File: mini_insta/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: defines the view functions and/or class-based views for the Django application.

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . models import *
from . forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

class MyLoginRequiredMixer(LoginRequiredMixin):
    """
    Verify that the current user is authenticated.
    """

    def get_login_url(self):
        """
        brings you to login page
        """
        return reverse('login')

    def get_logged_in_profile(self):
        """
        Returns the Profile object associated with the currently logged-in user.
        """
        return self.request.user.profile

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

    def get_object(self, queryset=None):
        """
        gets the profile object
        """
        if 'pk' in self.kwargs:
            return Profile.objects.get(pk=self.kwargs['pk'])
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        """
        allows template to access the current profile thats logged in
        """
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['current_profile'] = Profile.objects.get(user=self.request.user)
        else:
            context['current_profile'] = None
        return context

class PostDetailView(DetailView):
    """
    Displays a single post
    """
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        """
        allows the post template to see if the logged in user has liked the post already
        """
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        current_profile = Profile.objects.get(user=self.request.user)
        is_liked = post.get_likes().filter(profile=current_profile).exists()
        context['is_liked'] = is_liked

        return context

class CreatePostView(MyLoginRequiredMixer, CreateView):
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
        # pk = self.kwargs['pk']
        # profile = Profile.objects.get(pk=pk)
        user = self.request.user
        profile = Profile.objects.get(user=user)

        context['profile'] = profile

        return context

    def form_valid(self, form):
        """
        Handles the form submission and processes the data.
        """
        # attaching foreign key and attaching it to the instance
        print(form.cleaned_data)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.profile = profile

        post = form.save()

        # attaching photo to post

        # image_url = self.request.POST.get('image_url')
        # if image_url:
        #     photo = Photo(post=post, image_url=image_url)
        #     photo.save()

        files = self.request.FILES.getlist('files')
        for file in files:
            photo = Photo(post=post, image_file=file)
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

    def get_object(self):
        """
        gets the profile object
        """
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return profile

class UpdateProfileView(MyLoginRequiredMixer, UpdateView):
    '''A view to update an profile and save it to the database.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def form_valid(self, form):
        '''
        Handle the form submission to create a new profile object.
        '''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)

    def get_object(self):
        """
        gets the profile object
        """
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return profile

class DeletePostView(MyLoginRequiredMixer, DeleteView):
    """
    A view to delete a comment and remove it from the database.
    """

    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_context_data(self, **kwarg):
        """
        will provide the context data needed to support the delete_post_form.html
        """
        context = super().get_context_data(**kwarg)
        pk = self.kwargs['pk']

        # get post
        post = Post.objects.get(pk=pk)

        # get profile
        profile = post.profile

        context['post'] = post
        context['profile'] = profile
        return context

    def get_success_url(self):
        """
        Redirects to the Profile
        """
        # return a url of what to do after success
        pk = self.object.profile.pk
        # reverse builds url
        return reverse('profile', kwargs={'pk': pk})

class UpdatePostView(MyLoginRequiredMixer, UpdateView):
    """
    A view to update an post and save it to the database.
    """

    model = Post
    template_name = "mini_insta/update_post_form.html"
    form_class = UpdatePostForm

    def form_valid(self, form):
        '''
        Handle the form submission to create a new post object.
        '''
        print(f'UpdatePostView: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the post detail page after updating.
        """
        return reverse('post', kwargs={'pk': self.object.pk})

class ShowFollowersDetailView(DetailView):
    """
    provide the context variable profile to the show followers template
    """

    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    """
    provide the context variable profile to the show following template
    """

    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

class PostFeedListView(MyLoginRequiredMixer, ListView):
    """
    View for our feed page
    """

    model = Post
    template_name = "mini_insta/show_feed.html"
    context_object_name = "posts"

    def get_context_data(self):
        """
        Adds the profile object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        # pk = self.kwargs['pk']
        # profile = Profile.objects.get(pk=pk)

        user = self.request.user
        profile = Profile.objects.get(user=user)
        context['profile'] = profile

        return context

    def get_object(self):
        """
        gets the profile object
        """
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return profile

class SearchView(MyLoginRequiredMixer, ListView):
    """
    View for our search engine
    """

    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profile"

    def get_context_data(self):
        """
        Adds the profile object to the template context based on
        the `pk` provided in the URL.
        """
        context = super().get_context_data()
        query = self.request.GET.get("query")

        if query:
            context['query'] = query
            context['profiles'] = Profile.objects.filter(
                Q(username__icontains=query) |
                Q(display_name__icontains=query) |
                Q(bio_text__icontains=query)
            )
            context['posts'] = Post.objects.filter(caption__icontains=query)

        context['profile'] = Profile.objects.get(user = self.request.user)

        return context

    def dispatch(self, request, *args, **kwargs):
        """overrides the super method to handle any request"""

        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        if 'query' not in request.GET:
            profile = Profile.objects.get(user = self.request.user)
            return render(request, 'mini_insta/search.html', {'profile': profile})
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        obtains the QuerySet of instance data
        """
        # testing

        query = self.request.GET.get("query")

        if not query:
            return Post.objects.none()

        return Post.objects.filter(caption__icontains=query)

    def get_object(self):
        """
        gets the profile object
        """
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return profile

class LogOutView(TemplateView):
     """
     view for logging out
     """
     template_name = "mini_insta/logged_out.html"

class CreateProfileView(CreateView):
    """
    view for creating a new profile
    """
    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"
    model = Profile

    def get_context_data(self, **kwargs):
        """
        adding user form to context
        """
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        """
        when the form is submitted we want to save and log the user in
        """
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():

            user = user_form.save()
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            form.instance.user = user

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class FollowProfileView(MyLoginRequiredMixer, TemplateView):
    """
    view for following a profile
    """
    def dispatch(self, request, *args, **kwargs):
        """
        handles the following process
        """
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        current_profile = Profile.objects.get(user=request.user)

        if current_profile != target_profile:
            Follow(follower_profile=current_profile, profile=target_profile).save()
        url = reverse('profile', kwargs={'pk': target_profile.pk})
        return redirect(url)

class UnfollowProfileView(MyLoginRequiredMixer, TemplateView):
    """
    view for unfollowing a profile
    """

    def dispatch(self, request, *args, **kwargs):
        """
        deleting the instance of that follow
        """
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        current_profile = Profile.objects.get(user=request.user)

        Follow.objects.filter(follower_profile=current_profile, profile=target_profile).delete()
        url = reverse('profile', kwargs={'pk': target_profile.pk})
        return redirect(url)

class LikePostView(MyLoginRequiredMixer, TemplateView):
    """
    view for liking a post
    """

    def dispatch(self, request, *args, **kwargs):
        """
        handles the liking process
        """
        post = Post.objects.get(pk=kwargs['pk'])
        current_profile = Profile.objects.get(user=request.user)

        if post.profile != current_profile:
            Like(profile=current_profile, post=post).save()
        url = reverse('post', kwargs={'pk': post.pk})
        return redirect(url)

class UnlikePostView(MyLoginRequiredMixer, TemplateView):
    """
    view for unliking a post
    """

    def dispatch(self, request, *args, **kwargs):
        """
        deletes the instance of that like"""
        post = Post.objects.get(pk=kwargs['pk'])
        current_profile = Profile.objects.get(user=request.user)

        Like.objects.filter(profile=current_profile, post=post).delete()
        url = reverse('post', kwargs={'pk': post.pk})
        return redirect(url)