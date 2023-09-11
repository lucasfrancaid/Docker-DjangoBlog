from django.urls import reverse_lazy
from django.views import generic

from blog.apps.authors.forms import AuthorForm
from blog.apps.authors.models import Author
from blog.mixins import AdminPermissionRequiredMixin


class ListView(AdminPermissionRequiredMixin, generic.ListView):
    permission_required = "authors.view_author"
    model = Author
    template_name = "authors/list.html"
    context_object_name = "authors"


class DetailView(generic.DetailView):
    model = Author
    template_name = "authors/read.html"
    context_object_name = "author"


class CreateView(AdminPermissionRequiredMixin, generic.FormView, generic.CreateView):
    permission_required = "authors.add_author"
    template_name = "authors/form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class UpdateView(AdminPermissionRequiredMixin, generic.FormView, generic.UpdateView):
    permission_required = "authors.change_author"
    template_name = "authors/form.html"
    form_class = AuthorForm
    context_object_name = "author"
    success_url = reverse_lazy("index")
    queryset = Author.objects.all()

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class DeleteView(AdminPermissionRequiredMixin, generic.DeleteView):
    permission_required = "authors.delete_author"
    model = Author
    success_url = reverse_lazy("index")
    template_name = "authors/confirm_delete.html"
    template_name_suffix = ""
    context_object_name = "author"
