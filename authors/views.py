from django.urls import reverse_lazy
from django.views import generic
from authors.models import Author
from authors.forms import AuthorForm


class ListView(generic.ListView):
    model = Author
    template_name = "authors/list.html"
    context_object_name = "authors"


class DetailView(generic.DetailView):
    model = Author
    template_name = "authors/read.html"
    context_object_name = "author"


class CreateView(generic.FormView, generic.CreateView):
    template_name = "authors/form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class UpdateView(generic.FormView, generic.UpdateView):
    template_name = "authors/form.html"
    form_class = AuthorForm
    context_object_name = "author"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.is_valid()
        return super().form_valid(form)


class DeleteView(generic.DeleteView):
    model = Author
    success_url = reverse_lazy("index")
