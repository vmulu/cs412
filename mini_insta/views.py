# File: mini_insta/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: defines the view functions and/or class-based views for the Django application.

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Profile, Post, Photo
from . forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.db.models import Q

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

class UpdateProfileView(UpdateView):
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

class DeletePostView(DeleteView):
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

class UpdatePostView(UpdateView):
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

class PostFeedListView(ListView):
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
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile

        return context

class SearchView(ListView):
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

        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])

        return context

    def dispatch(self, request, *args, **kwargs):
        """overrides the super method to handle any request"""

        if 'query' not in request.GET:
            profile = Profile.objects.get(pk=self.kwargs['pk'])
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
