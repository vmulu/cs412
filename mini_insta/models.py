# File: mini_insta/models.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 9/23/2025
# Description: Defines the data models for the Django application.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """
    Represents a user's profile in the application.
    """

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    join_date = models.DateTimeField(auto_now=True)
    bio_text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'username: {self.username} name: {self.display_name}'

    def get_all_posts(self):
        """
        finds and returns all Posts for a given Profile
        """
        posts = Post.objects.filter(profile=self)
        return posts

    def get_absolute_url(self):
        """
        returns the URL corresponding to the Profile
        """
        return reverse('profile', kwargs={'pk': self.pk})

    def get_followers(self):
        """
        returns how many followers this instance has
        """
        followers = Follow.objects.filter(profile=self)
        followers_lst = []

        for follow in followers:
            followers_lst.append(follow.follower_profile)

        return followers_lst

    def get_num_followers(self):
        """
        return the count of followers.
        """

        followers_lst = self.get_followers()

        return len(followers_lst)

    def get_following(self):
        """
        return a list of those Profiles followed by this profile
        """
        following = Follow.objects.filter(follower_profile=self)
        following_lst = []

        for follow in following:
            following_lst.append(follow.profile)

        return following_lst

    def get_num_following(self):
        """
        return the count of how many profiles are being followed.
        """

        following_lst = self.get_following()

        return len(following_lst)

    def get_post_feed(self):
        """
        will return a list (or QuerySet) of Posts specifically for the profiles
        being followed by the profile
        """
        posts = []
        for profile in self.get_following():
            for post in profile.get_all_posts():
                posts.append(post)

        return posts

class Post(models.Model):
    """
    Represents a user's post on their profile
    """

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.caption}'

    def get_all_photos(self):
        """
        finds and returns all Photos for a given Post.
        """
        photos = Photo.objects.filter(post=self).order_by('timestamp')
        return photos

    def get_all_comments(self):
        """
        retrieves all comments on a Post
        """
        comments = Comment.objects.filter(post=self)
        return comments

    def get_likes(self):
        """
        retrieve all likes on a Post
        """
        likes = Like.objects.filter(post=self)
        return likes

class Photo(models.Model):
    """
    Represents the data attributes of an image associated with a Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        if self.image_url:
            image_source = self.image_url
        elif self.image_file:
            image_source = self.image_file.url
        else:
            image_source = "No image available"

        return f'photo for {self.post} image URL: {image_source}'

    def get_image_url(self):
        """
        Returns the URL to the image, will either be the URL stored in the
        image_url attribute (if it exists), or else the URL to the image_file attribute
        """
        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url

class Follow(models.Model):
    """
    encapsulates the idea of an edge connecting two nodes within the social network
    """

    # indicating which profile is being followed
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    # indicating which profile is doing the following
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.follower_profile.display_name} follows {self.profile.display_name}'

class Comment(models.Model):
    """
    encapsulates the idea of one Profile providing a response or commentary on a Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        return f"{self.profile.username} commented on {self.post.profile}'s post"

class Like(models.Model):
    """
    encapsulates the idea of one Profile providing approval of a Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile.username} likes {self.post.profile.username} post'