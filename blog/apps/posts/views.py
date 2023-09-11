import requests
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic

from blog.apps.posts.forms import PostForm
from blog.apps.posts.models import Post, View
from blog.mixins import AdminPermissionRequiredMixin


class ListView(AdminPermissionRequiredMixin, generic.ListView):
    permission_required = "posts.view_post"
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/read.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        self._add_view_from_ip()
        return super().get_context_data(**kwargs)

    def _add_view_from_ip(self) -> None:
        ip_address = (
            self.request.META.get("HTTP_X_FORWARDED_FOR")
            or self.request.META.get("REMOTE_ADDR", "")
        ).split(",")[0]

        response = requests.get(settings.IP_LOCATION_API.format(ip_address=ip_address))
        geo_ip = response.json()

        View(
            post_id=self.object.id,
            latitude=geo_ip.get("lat") or geo_ip.get("latitude", 37.4267861),
            longitude=geo_ip.get("lon") or geo_ip.get("longitude", -122.0806032),
            ip_address=ip_address,
        ).save()


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
