from django.views import generic

from posts.models import Post


class IndexView(generic.ListView):
    template_name = "index.html"

    def get_queryset(self):
        if search := self.request.GET.get('search'):
            return Post.objects.filter(title__icontains=search)
        return Post.objects.order_by("-likes")[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['search_value'] = self.request.GET.get('search')
        return context
