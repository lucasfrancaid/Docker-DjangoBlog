from django.urls import reverse_lazy
from django.views import generic

from blog.mixins import AdminPermissionRequiredMixin
from posts.models import Post
from posts.forms import PostForm


class ListView(AdminPermissionRequiredMixin, generic.ListView):
    permission_required = "posts.view_post"
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/read.html"
    context_object_name = "post"


class CreateView(AdminPermissionRequiredMixin, generic.FormView, generic.CreateView):
    permission_required = "posts.add_post"
    template_name = "posts/form.html"
    form_class = PostForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class UpdateView(AdminPermissionRequiredMixin, generic.FormView, generic.UpdateView):
    permission_required = "posts.change_post"
    template_name = "posts/form.html"
    form_class = PostForm
    context_object_name = "post"
    success_url = reverse_lazy("index")
    queryset = Post.objects.all()

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class DeleteView(AdminPermissionRequiredMixin, generic.DeleteView):
    permission_required = "posts.delete_post"
    model = Post
    success_url = reverse_lazy("index")
    template_name = "posts/confirm_delete.html"
    template_name_suffix = ""
    context_object_name = "post"
