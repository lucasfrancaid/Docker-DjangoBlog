from typing import Any
from django.db import models
from django.urls import reverse_lazy
from django.views import generic

from posts.models import Post
from posts.forms import PostForm


class ListView(generic.ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/read.html"
    context_object_name = "post"


class CreateView(generic.FormView, generic.CreateView):
    template_name = "posts/form.html"
    form_class = PostForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class UpdateView(generic.FormView, generic.UpdateView):
    template_name = "posts/form.html"
    form_class = PostForm
    context_object_name = "post"
    success_url = reverse_lazy("index")
    queryset = Post.objects.all()

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index")
