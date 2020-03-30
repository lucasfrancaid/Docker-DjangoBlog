from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField(max_length=200)
