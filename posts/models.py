from django.db import models

from authors.models import Author


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    background_url = models.URLField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.author.full_name}"


class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    latitute = models.FloatField()
    longitude = models.FloatField()
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
