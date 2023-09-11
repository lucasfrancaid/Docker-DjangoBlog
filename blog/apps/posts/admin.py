from django.contrib import admin

from blog.apps.posts.models import Post, View

admin.site.register(Post)
admin.site.register(View)
