from django import forms

from blog.apps.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["background_url", "title", "subtitle", "body", "author"]
